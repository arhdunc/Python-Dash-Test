LLM Instruction (Header): This guide defines the visual style, layout, and component conventions for Shiny dashboards in this project. Apply these standards meticulously when generating UI code, plots, or other visual elements.

# 1. Layout

*   **Default Structure**: Use `ui.layout_sidebar()` as the primary layout for most dashboards.
*   **Sidebar Width**: `ui.sidebar(width="...")`: **300px**
*   **Main Panel**: Ensure adequate spacing for content.
*   **Page Function**: Use `ui.page_fluid()` as the top-level page container unless a fixed layout (`ui.page_fixed()`) is explicitly required.
*   **Arrangement**: Place primary filters and controls in the sidebar. Display primary outputs (plots, tables) in the main panel. Use `ui.layout_columns()` or `ui.layout_rows()` for arranging multiple outputs if needed.

# 2. Styling (Colors, Fonts, Spacing)

*(Leverage bslib themes if integrated, otherwise use custom CSS concepts)*

*   **Colors**:
    *   Primary Brand Color: **#007bff** (Used for headers, active elements)
    *   Secondary Brand Color: **#6c757d** (Used for accents, highlights)
    *   Background Color: **#f8f9fa**
    *   Text Color: **#212529**
    *   Plotly Chart Palette (Categorical): **px.colors.qualitative.Plotly**
    *   Plotly Chart Palette (Sequential): **px.colors.sequential.Viridis**
*   **Fonts**:
    *   Primary Font Family: **"Helvetica Neue", Helvetica, Arial, sans-serif**
    *   Body Text Size: **1rem**
    *   Heading Font Weight: **bold**
    *   Plot Font Family: **"Helvetica Neue", Helvetica, Arial, sans-serif**
*   **Spacing**:
    *   Default Padding (around elements like inputs, plots): **15px**
    *   Margin Between Components (e.g., between two plots): **20px**
    *   Sidebar Padding: **15px**

# 3. Component Conventions

*   **Inputs (`ui.input_*`)**: Ensure clear labels positioned appropriately (e.g., above the control). Use consistent width where possible within the sidebar.
*   **Buttons (`ui.input_action_button`)**: Use the primary brand color unless it signifies a destructive action. Use clear, concise labels.
*   **Tables (`ui.output_data_frame` / `render.DataGrid`)**: Use clear headers. Consider enabling filtering/sorting options with `render.DataGrid` for interactive tables. Apply subtle striping or borders for readability.
*   **Value Boxes/Cards (`ui.value_box` if used)**: Use consistent styling for icons, values, and titles. Align with brand colors.

# 4. Plotting (Plotly Specific)

*   **Default Theme/Template**: Use Plotly template: **plotly_white**
*   **Titles & Labels**: All plots MUST have informative titles and clear axis labels. Use the primary font family specified above.
*   **Legends**: Position legends appropriately (e.g., top-right, bottom-right) and ensure they are readable.
*   **Tooltips/Hover Info**: Provide informative hover text, clearly indicating the data point and its value(s).
*   **Color Mapping**: Use the specified chart palettes (categorical/sequential) consistently.
*   **Annotations/Source**: Include data source or explanatory notes directly on the plot or below it where necessary. Use a smaller font size for source notes.