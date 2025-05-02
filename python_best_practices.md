LLM Instruction (Header): This document outlines Python best practices and library conventions for this project. Adhere to these guidelines STRICTLY when generating or modifying Python code.

# General Python Best Practices

*   **Formatting**: Adhere to PEP 8 guidelines for code style, including 4-space indentation, maximum line length (e.g., 79 or 99 characters), and appropriate use of whitespace. Use a code formatter like Black if possible.
*   **Naming Conventions**: Use `snake_case` for variables and functions. Use `PascalCase` for classes. Choose descriptive names.
*   **Docstrings**: Write clear docstrings for all modules, classes, functions, and methods using a standard format (e.g., Google style or NumPy style). Explain what the code does, its arguments, and what it returns.
*   **Error Handling**: Use `try...except` blocks appropriately to handle potential errors gracefully. Avoid bare `except:` clauses.
*   **Imports**: Place all imports at the top of the file, grouped into standard library, third-party, and local application imports.
*   **Scope**: Avoid unnecessary use of global variables, especially within Shiny server functions. Pass data explicitly.

# Library Usage - Polars vs. Pandas

*   **Project Standard**: Use **Polars** for all DataFrame operations. Avoid Pandas unless explicitly instructed for a specific compatibility reason.

## Key Differences & Examples:

*   **Reading Data**:
    *   Polars: `pl.read_csv("data.csv")`
    *   Pandas: `pd.read_csv("data.csv")`
*   **Selecting Columns**:
    *   Polars: `df.select("col_a", "col_b")` or `df.select(pl.col("col_a"))`
    *   Pandas: `df[["col_a", "col_b"]]` or `df.loc[:, ["col_a", "col_b"]]`
*   **Filtering Rows**:
    *   Polars: `df.filter(pl.col("age") > 30)` or `df.filter((pl.col("category") == "A") & (pl.col("value") > 10))`
    *   Pandas: `df[df["age"] > 30]` or `df[(df["category"] == "A") & (df["value"] > 10)]`
*   **Grouping and Aggregating**:
    *   Polars: `df.group_by("category").agg(pl.sum("value"), pl.mean("score").alias("avg_score"))`
    *   Pandas: `df.groupby("category").agg(value_sum=('value', 'sum'), avg_score=('score', 'mean'))`
*   **Mutability**: Polars DataFrames are generally immutable (operations return new DataFrames), promoting safer data handling compared to Pandas' potential for in-place modifications.
*   **Expressions**: Polars heavily uses an expression API (`pl.col()`, `pl.sum()`, etc.) which allows for optimization and parallel execution (lazy evaluation). Understand and leverage this API.

# Library Usage - Shiny for Python

*   **Structure**: Prefer the standard UI/Server separation (`app_ui = ui.page_fluid(...)`, `def server(input, output, session):`) for applications beyond simple examples. Avoid mixing UI and server logic excessively (as sometimes seen in Shiny Express examples) for better maintainability.
*   **Reactivity**: Keep reactive expressions (`@render.plot`, `@reactive.calc`, etc.) focused on a single task. Avoid overly complex reactive chains.
*   **Modularity**: For larger apps, utilize Shiny Modules (`@module.ui`, `@module.server`) to encapsulate related UI and server logic, improving organization and reusability.
*   **Efficiency**: Perform expensive computations outside reactive contexts if they don't need to update frequently, or use caching mechanisms (`@reactive.calc(cache=...)` if applicable and appropriate).

# Plotting

*   **Default Library**: Use **Plotly** for creating interactive visualizations unless otherwise specified.
*   **Consistency**: Adhere to the project's `style_guide.md` for plot themes, colors, fonts, and layout conventions.
*   **Clarity**: Ensure plots have clear titles, axis labels, and legends.