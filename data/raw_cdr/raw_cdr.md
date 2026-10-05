# Raw CDR Data

This directory is reserved for the raw and preprocessed Call Detail Record (CDR) datasets used by the project.

The original files have been removed from the public repository because they contain non-public telecommunications data.

## Expected contents

The original project used files corresponding to:

- Raw CDR data
- Cleaned CDR data
- Fraud-labelled CDR data
- Normal CDR data
- Additional CDR samples used during development

The exact filenames and processing steps can be found in the preparation notebooks under:

```text
notebooks/#0_prepare/
```

In particular:

```text
01_duckdb_setup.ipynb
02_manual_eda.ipynb
03_sweetviz_eda.ipynb
04_preprocessing.ipynb
05_profiling_and_feature_extraction.ipynb
```

## Public repository status

No CDR records are distributed with this repository.