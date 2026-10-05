# Source Code

This directory contains the project's reusable application code.

## Contents

### `streamlit_app.py`

Provides the Streamlit interface used for interacting with the project's DuckDB-based exploratory workflow.

The application was developed to facilitate querying and inspecting the project data during analysis.

## Data dependency

The application expects access to the project datasets and local DuckDB database.

These data files are intentionally excluded from the public repository because the underlying telecommunications data is non-public.

The database setup and data preparation workflow are documented in:

```text
notebooks/#0_prepare/
```

In particular:

```text
notebooks/#0_prepare/01_duckdb_setup.ipynb
```

and the local database is documented under:

```text
database/
```