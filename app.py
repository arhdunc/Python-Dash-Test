"""
Shiny dashboard for case volume analysis.
- Uses Polars for data operations (per python_best_practices.md)
- UI and plot styling per style_guide.md
- Follows shiny_dashboard_flow.md structure
"""

# Standard library imports
import os

# Third-party imports
import polars as pl
import plotly.express as px
from shiny import App, ui, render, reactive

# Data loading (Step 2.1)
DATA_PATH = "Fake_Data.csv"
def load_data():
    try:
        df = pl.read_csv(DATA_PATH, try_parse_dates=True)
        return df
    except FileNotFoundError:
        raise RuntimeError(f"Data file not found: {DATA_PATH}")

df = load_data()

# Prepare filter choices (Step 2.2)
def get_unique_choices(df, col):
    vals = df.get_column(col).unique().to_list()
    vals = [v for v in vals if v is not None and v != ""]
    vals.sort()
    return vals

main_category_choices = get_unique_choices(df, "Main Category")
status_choices = get_unique_choices(df, "Status")

# UI Layout (Step 3.1, 3.2, 4.1, 4.3)
app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "main_category",
                "Main Category:",
                choices=["All"] + main_category_choices,
                width="100%"
            ),
            ui.input_select(
                "status",
                "Status:",
                choices=["All"] + status_choices,
                width="100%"
            ),
            ui.input_action_button(
                "update_btn",
                "Update",
                class_="btn btn-primary",
                width="100%"
            ),
            width="300px",
            style="padding:15px; background-color:#f8f9fa;"
        ),
        ui.layout_columns(
            ui.output_text("total_cases"),
            widths=12,
            style="margin-bottom:20px;"
        ),
        ui.output_plot("cases_over_time", height="400px"),
        style="padding:15px;"
    )
)

# Server logic (Step 4.2, 4.4)
def server(input, output, session):
    @reactive.calc
    def filtered_df():
        # Only update when button is clicked
        input.update_btn()
        dff = df
        if input.main_category() != "All":
            dff = dff.filter(pl.col("Main Category") == input.main_category())
        if input.status() != "All":
            dff = dff.filter(pl.col("Status") == input.status())
        return dff

    @output
    @render.text
    def total_cases():
        dff = filtered_df()
        total = dff.get_column("Unique Case ID").n_unique()
        return f"Total Unique Cases: {total}"

    @output
    @render.plotly
    def cases_over_time():
        dff = filtered_df()
        # Group by Product and count unique cases
        product_counts = dff.group_by("Product").agg(
            pl.col("Unique Case ID").n_unique().alias("Case Volume")
        ).sort("Case Volume", descending=True)
        # Only select columns needed for plotting and ensure correct dtypes
        plot_df = product_counts.select(["Product", "Case Volume"]).to_pandas().copy()
        plot_df = plot_df.reset_index(drop=True)
        plot_df["Product"] = plot_df["Product"].astype(str)
        plot_df["Case Volume"] = plot_df["Case Volume"].astype(int)
        # Handle empty data gracefully
        if plot_df.empty:
            import plotly.graph_objects as go
            fig = go.Figure()
            fig.add_annotation(
                text="No data available for the selected filters.",
                xref="paper", yref="paper", showarrow=False,
                font=dict(size=16, color="#6c757d")
            )
            fig.update_layout(
                template="plotly_white",
                plot_bgcolor="#f8f9fa",
                paper_bgcolor="#f8f9fa",
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                margin=dict(l=20, r=20, t=60, b=40)
            )
            return fig
        # Plotly styling per style_guide.md
        import plotly.express as px
        fig = px.bar(
            plot_df,
            x="Product",
            y="Case Volume",
            title="Unique Case Volume by Product",
            template="plotly_white",
            color_discrete_sequence=["#007bff"],
        )
        fig.update_layout(
            font_family="Helvetica Neue, Helvetica, Arial, sans-serif",
            font_color="#212529",
            title_font=dict(size=20, family="Helvetica Neue, Helvetica, Arial, sans-serif", color="#007bff"),
            plot_bgcolor="#f8f9fa",
            paper_bgcolor="#f8f9fa",
            margin=dict(l=20, r=20, t=60, b=40),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        fig.update_xaxes(title="Product", showgrid=True)
        fig.update_yaxes(title="Unique Cases", showgrid=True)
        return fig

app = App(app_ui, server)
