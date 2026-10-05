# Notebooks

This directory contains the Jupyter notebooks used throughout the SIMBox fraud detection project.

The notebooks are organized by **project stage and experimental pipeline**, separating data preparation, model development under different validation strategies, and investigation of the gap between the independently obtained results and the historical benchmark.

## Structure

```text
notebooks/
├── gap_investigation/
│   ├── 01_diagnostic_profiling.ipynb
│   ├── 02_diagnostic_filtering.ipynb
│   ├── 03_reconstruct_og_dates_and_split.ipynb
│   └── 04_og_results_recreation.ipynb
├── 03_sgkf_rv_label_day_new_feats/
│   ├── 05_profiling_and_feature_extraction_v2.ipynb
│   ├── 06_dataset_versioning_v5.ipynb
│   ├── 07_feature_engineering_v5.ipynb
│   ├── 08_model_training.ipynb
│   ├── 09_hyperparameter_tuning.ipynb
│   └── 10_final_training_and_evaluation.ipynb
├── 02_rolling_day/
│   ├── 06_dataset_versioning_v4.ipynb
│   ├── 07_feature_engineering_v4.ipynb
│   ├── 08_model_training.ipynb
│   ├── 09_hyperparameter_tuning.ipynb
│   └── 10_final_training_and_evaluation.ipynb
├── 01_sgkf_msisdn/
│   ├── 06_dataset_versioning_v1_v2.ipynb
│   ├── 07_feature_engineering_v1.ipynb
│   ├── 07_feature_engineering_v2_v3.ipynb
│   ├── 08_model_training.ipynb
│   ├── 09_hyperparameter_tuning.ipynb
│   └── 10_final_training_and_evaluation.ipynb
└── 00_preparation/
    ├── 01_duckdb_setup.ipynb
    ├── 02_manual_eda.ipynb
    ├── 03_sweetviz_eda.ipynb
    ├── 04_preprocessing.ipynb
    └── 05_profiling_and_feature_extraction.ipynb
```

## Notebook Groups

### `00_preparation/`

Initial data preparation and exploratory analysis.

- `01_duckdb_setup.ipynb` — Sets up the DuckDB environment used for exploratory querying.
- `02_manual_eda.ipynb` — Manual exploratory data analysis of the CDR datasets.
- `03_sweetviz_eda.ipynb` — Automated exploratory analysis using Sweetviz.
- `04_preprocessing.ipynb` — Data cleaning and preprocessing.
- `05_profiling_and_feature_extraction.ipynb` — Creates daily MSISDN-level profiles and extracts behavioral features.

### `01_sgkf_msisdn/`

First main modeling pipeline using **Stratified Group K-Fold (SGKF)** validation with MSISDN as the grouping variable.

The notebooks cover dataset versioning, feature engineering, model training, hyperparameter tuning, and final evaluation.

The feature-engineering notebooks retain their version identifiers because they represent distinct iterations of the feature-development process.

### `02_rolling_day/`

Alternative modeling pipeline using a **rolling-day validation strategy**.

This experiment evaluates the model under a temporal validation setup while retaining the same general training, tuning, and evaluation workflow.

### `03_sgkf_rv_label_day_new_feats/`

Later modeling pipeline combining the revised validation/label setup with additional feature engineering.

This directory contains the corresponding profiling, dataset versioning, feature engineering, training, tuning, and final evaluation notebooks.

### `gap_investigation/`

Investigation of the discrepancy between the independently obtained model performance and the historical benchmark.

The notebooks document the diagnostic work used to examine differences in profiling, filtering, dates, data splits, labels, and historical results.

- `01_diagnostic_profiling.ipynb` — Diagnostic comparison of profiling outputs and populations.
- `02_diagnostic_filtering.ipynb` — Investigation of filtering conditions and their effect on the modeling population.
- `03_reconstruct_og_dates_and_split.ipynb` — Reconstruction of the historical date ranges and dataset split.
- `04_og_results_recreation.ipynb` — Recreation of the historical modeling conditions and results.

## Execution

The notebooks are intended to be executed in their respective project order rather than as a single linear sequence.

The required datasets and generated artifacts are **not included in the public repository**. Some notebooks therefore require access to the original project data and locally generated artifacts to run completely.

The notebooks are retained as a record of the project's experimental workflow, model development, validation experiments, and historical-pipeline investigation.