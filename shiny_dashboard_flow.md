LLM Instruction (Header): This document provides a step-by-step flow for creating components of a Shiny for Python dashboard. Follow these steps sequentially when requested to build dashboard elements. Always refer to style_guide.md and python_best_practices.md as indicated.

# Shiny Dashboard Creation Flow

**Objective**: Guide the LLM through building a standard Shiny dashboard component by component. Always refer to `style_guide.md` for UI/styling and `python_best_practices.md` for code conventions.

## Step 1: Setup and Boilerplate (If starting new file/component)

*   **Task**: Create the basic `app.py` file structure (or module structure) with necessary imports (e.g., `shiny`, `polars`, `plotly.express as px`). Define the initial `ui` layout (e.g., `ui.page_fluid` with `ui.layout_sidebar`) and empty `server` function.
*   **Check**: `python_best_practices.md` for standard imports and structure.

## Step 2: Add Input Control(s) to UI

*   **Task**: Add the specified `ui.input_...()` function to the UI layout (typically within a `ui.sidebar` or other designated area). Assign the unique `id`, `label`, `choices`/`range`, and default `value` as requested by the user.
*   **Check**: `style_guide.md` for preferred input control layout, styling, and placement conventions.
*   **Check**: Ensure the `id` is unique within the application/module.

## Step 3: Add Output Placeholder(s) to UI

*   **Task**: Add the specified `ui.output_...()` function (e.g., `ui.output_plot`, `ui.output_data_frame`) to the UI layout (typically the main panel). Assign the unique `id` that will link to the server logic.
*   **Check**: `style_guide.md` for preferred output element spacing and layout.
*   **Check**: Ensure the `id` is unique within the application/module.

## Step 4: Implement Server Logic for Output

*   **Task**: Implement the `@render.output_type` (e.g., `@render.plot`, `@render.data_frame`) decorated function within the `server` function (or module server). The function name should ideally match the output `id` for clarity (e.g., `@render.plot def my_plot():` corresponds to `ui.output_plot("my_plot")`).
*   **Inside the function**:
    *   Read necessary `input.input_id()` values reactively. Ensure inputs are accessed inside the render function to establish dependency.
    *   Load/prepare data. Use **Polars** for all DataFrame operations.
    *   Perform calculations/filtering based on the reactive input values.
    *   Generate the output object (e.g., a Plotly figure object, a Polars DataFrame).
    *   Return the output object.
*   **Check**: `python_best_practices.md` for correct Polars usage and general Python best practices.
*   **Check**: `style_guide.md` for required plot styling (themes, colors, fonts) if generating a plot.
*   **Check**: Ensure the function returns the correct object type for the `@render` decorator used.

## Step 5: Testing and Refinement

*   **Task**: Review the generated code for correctness, efficiency, and adherence to all guidelines. Add basic checks or request unit tests for the implemented server logic if specified in the project roadmap or requested by the user. Address any errors or inconsistencies.