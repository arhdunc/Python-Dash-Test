# Project Roadmap: <Dashboard Name/Feature>

**Goal:** <Briefly describe the primary objective of this dashboard/feature.>
**Key Data Source(s):** <List the main data files or databases used.>
**Primary Libraries:** Polars, Shiny, Plotly

---

## LLM Instructions for Roadmap Use:

*   Follow this roadmap step-by-step for project tasks assigned to you.
*   Before generating code for a step, state which step number and task you are addressing.
*   Explicitly confirm checking the specified context documents (`python_best_practices.md`, `style_guide.md`, `shiny_dashboard_flow.md`) when indicated by a '***Check:***' instruction below the task.
*   Ask for clarification if a step or requirement is unclear. Do not proceed with ambiguity.
*   When modifying existing code, clearly state which file and function/section you are modifying.

---

## Phase 1: Planning & Setup

*   [ ] **Task 1.1:** Define key metrics, calculations, and visualizations required for the dashboard. *(User Task)*
*   [ ] **Task 1.2:** Sketch basic UI layout (sidebar controls, main panel outputs). *(User Task)*
*   [ ] **Task 1.3:** Set up project directory structure. Create initial `app.py` with standard imports (`shiny`, `polars as pl`, `plotly.express as px`) and basic UI (`ui.page_fluid`, `ui.layout_sidebar`) / Server (`def server(input, output, session): pass`) structure.
    *   **LLM Action:** Generate the initial `app.py` boilerplate code.
    *   ***Check:*** `python_best_practices.md` for setup conventions and standard imports.

## Phase 2: Data Loading & Preparation

*   [ ] **Task 2.1:** Implement Polars function/logic within `app.py` (or a separate `data_loader.py` module if complex) to load data from `<Data Source Location e.g., "data/my_data.csv">`. Handle potential file not found errors.
    *   **LLM Action:** Write the Polars data loading code.
    *   ***Check:*** `python_best_practices.md` for Polars I/O best practices and error handling.
*   [ ] **Task 2.2:** Implement Polars logic for initial data cleaning and transformation needed globally for the dashboard (e.g., renaming columns, handling missing values, type conversions). Place this logic appropriately (e.g., after loading).
    *   **LLM Action:** Add Polars code for the specified cleaning/transformation tasks.
    *   ***Check:*** `python_best_practices.md` for Polars syntax, efficiency, and best practices.

## Phase 3: Core UI Controls

*   [ ] **Task 3.1:** Add primary input control 1: `<Specify ui.input type, e.g., ui.input_slider>` with `id='<input_id_1>'` to the UI sidebar. Configure `label="<Input 1 Label>"`, `choices`/`range`:`<Specify choices/range>`, `default value`:`<Specify default>`.
    *   **LLM Action:** Generate the UI code for this input control in `app.py`.
    *   ***Check:*** `style_guide.md` for input layout and styling.
    *   ***Check:*** `shiny_dashboard_flow.md` (Step 2) for guidance.
*   [ ] **Task 3.2:** Add primary input control 2: `<Specify ui.input type>` with `id='<input_id_2>'` to the UI sidebar. Configure `label="<Input 2 Label>"`, `choices`/`range`:`<Specify choices/range>`, `default value`:`<Specify default>`.
    *   **LLM Action:** Generate the UI code for this input control in `app.py`.
    *   ***Check:*** `style_guide.md` for input layout and styling.
    *   ***Check:*** `shiny_dashboard_flow.md` (Step 2) for guidance.
*   [ ] **** <Add more input tasks as needed> ****

## Phase 4: Core Outputs & Server Logic

*   [ ] **Task 4.1:** Add output placeholder 1: `<Specify ui.output type, e.g., ui.output_plot>` with `id='<output_id_1>'` to the UI main panel.
    *   **LLM Action:** Generate the UI code for this output placeholder in `app.py`.
    *   ***Check:*** `shiny_dashboard_flow.md` (Step 3) for guidance.
*   [ ] **Task 4.2:** Implement server logic for output `id='<output_id_1>'`. This function should:
    *   Reactively read inputs: `<List relevant input_ids, e.g., input.<input_id_1>()>`.
    *   Filter/aggregate the prepared Polars DataFrame based on inputs.
    *   Generate a `<Specify output type, e.g., Plotly bar chart>` using Plotly.
    *   Return the Plotly figure object.
    *   **LLM Action:** Create the `@render.plot` (or relevant type) function and implement the logic in `app.py`.
    *   ***Check:*** `shiny_dashboard_flow.md` (Step 4) for the process.
    *   ***Check:*** `python_best_practices.md` (Polars usage).
    *   ***Check:*** `style_guide.md` (Plotly styling).
*   [ ] **Task 4.3:** Add output placeholder 2: `<Specify ui.output type, e.g., ui.output_data_frame>` with `id='<output_id_2>'` to the UI main panel.
    *   **LLM Action:** Generate the UI code for this output placeholder in `app.py`.
    *   ***Check:*** `shiny_dashboard_flow.md` (Step 3) for guidance.
*   [ ] **Task 4.4:** Implement server logic for output `id='<output_id_2>'`. This function should:
    *   Reactively read inputs: `<List relevant input_ids>`.
    *   Perform necessary Polars aggregations/filtering based on inputs.
    *   Return the resulting Polars DataFrame (or object suitable for `render.DataGrid` etc.).
    *   **LLM Action:** Create the `@render.data_frame` (or relevant type) function and implement the logic in `app.py`.
    *   ***Check:*** `shiny_dashboard_flow.md` (Step 4) for the process.
    *   ***Check:*** `python_best_practices.md` (Polars usage).
    *   ***Check:*** `style_guide.md` (Table styling considerations if using DataGrid).
*   [ ] **** <Add more output tasks as needed> ****

## Phase 5: Styling & Refinement

*   [ ] **Task 5.1:** Review all UI code and Plotly plots generated so far. Ensure alignment with `style_guide.md` (colors, fonts, layout, spacing).
    *   **LLM Action:** Analyze specified code sections (UI layout, plot generation code) and suggest modifications to match the style guide. Implement approved changes.
    *   ***Check:*** `style_guide.md`.
*   [ ] **Task 5.2:** Implement user feedback mechanisms if needed (e.g., loading indicators for slow outputs). (Consider using libraries or custom CSS/JS).
    *   **LLM Action:** (If requested) Suggest or implement code for loading indicators.
*   [ ] **Task 5.3:** Perform thorough manual testing of all inputs and outputs. *(User Task)*
*   [ ] **Task 5.4:** Add comments and docstrings to complex sections of the server logic.
    *   **LLM Action:** Generate docstrings and comments for specified functions.
    *   ***Check:*** `python_best_practices.md` (Docstring conventions).

## Phase 6: Deployment (Placeholder)

*   [ ] Prepare deployment files (e.g., `requirements.txt`).
*   [ ] Configure deployment target (e.g., Posit Connect, Shinyapps.io, Docker).
*   [ ] Deploy application.