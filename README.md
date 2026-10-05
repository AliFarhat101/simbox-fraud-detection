# SIMBox Fraud Detection Using Machine Learning

Machine learning project for detecting **SIMBox fraud in telecommunications CDR data**.

The project investigates whether SIMBox-related fraudulent calling behavior can be detected from aggregated subscriber-level call patterns and develops an XGBoost-based classification pipeline for this purpose.

It also documents and investigates the discrepancy between independently obtained model performance and a historical benchmark associated with the original project workflow.

> **Project origin:** The project was originally provided by **Vanrise Solutions**. The implementation, experimentation, analysis, and documentation contained in this repository represent the author's work carried out during the project.

---

## Project Overview

SIMBox fraud is a form of telecommunications bypass fraud in which international traffic is routed through local SIM cards and presented to the network as local traffic.

This project applies machine learning to CDR data to identify subscriber-level behavioral patterns associated with SIMBox activity.

The workflow covers:

- CDR exploration and data quality analysis
- Data preprocessing
- Daily MSISDN-level profiling
- Behavioral feature engineering
- Feature selection and ablation analysis
- XGBoost classification
- Hyperparameter tuning
- Multiple validation strategies
- Precision-Recall AUC and ROC-AUC evaluation
- MLflow experiment tracking
- DVC-based dataset versioning
- Investigation of the discrepancy between independently obtained and historical results
- Reconstruction and documentation of the historical modeling pipeline

---

## Project Structure

```text
simbox-project/
│
├── data/                       # Data templates; actual datasets excluded
├── database/                   # Local database template
├── mlruns/                     # MLflow tracking directory template
├── notebooks/                  # Analysis and modeling notebooks
│   ├── 00_preparation/
│   ├── 01_sgkf_msisdn/
│   ├── 02_rolling_day/
│   ├── 03_sgkf_rv_label_day_new_feats/
│   └── gap_investigation/
├── reports/                    # EDA reports
├── src/                        # Application/source code
│   └── streamlit_app.py
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── .gitattributes
└── .env.example
```

The public repository intentionally excludes the original CDR data, generated profile datasets, database files, model prediction datasets, and MLflow run artifacts.

---

## Main Methodology

### 1. Data Preparation

Raw CDR data is cleaned and prepared for analysis. Data quality checks include missing-value inspection, duplicate analysis, class-label consistency, and identification of records appearing across the original datasets.

### 2. Subscriber Profiling

CDRs are aggregated into daily MSISDN-level profiles.

The profiling stage transforms individual call records into behavioral summaries that can be used by machine-learning models.

### 3. Feature Engineering

Behavioral features are derived from:

- Call volume
- Incoming/outgoing activity
- Contact diversity
- Call duration
- Repeated calling behavior
- Temporal activity
- Mobility
- Flagged-cell activity
- Other subscriber-level behavioral patterns

Feature analysis includes correlation analysis, XGBoost importance, SHAP analysis, and feature ablation.

### 4. Model Development

The primary classifier is **XGBoost** using a binary classification objective.

The project evaluates different dataset constructions and validation strategies rather than relying on a single train/test configuration.

### 5. Evaluation

The primary evaluation metric is **Average Precision / PR-AUC**, with ROC-AUC used as a complementary metric.

Classification reports and confusion matrices are also used where threshold-dependent analysis is required.

### 6. Historical Pipeline Investigation

A major part of the project investigates the difference between the independently obtained model performance and the historical benchmark associated with the original workflow.

The investigation examines:

- Profiling populations
- Filtering conditions
- Historical date ranges
- Dataset splits
- Label assignments
- Historical modeling conditions

The historical result could be reproduced under the reconstructed historical conditions, demonstrating that the discrepancy was related to differences in the underlying data and processing configuration rather than simply the choice of classifier.

---

## Reproducibility

The repository preserves the project workflow and notebooks while excluding the underlying telecommunications data and other data-derived artifacts.

To reproduce the complete workflow, authorized access to the original project data and required artifacts is necessary.

Some directories therefore contain `README.md` files describing the expected structure instead of the original files.

---

## Technologies

- Python
- Pandas
- NumPy
- DuckDB
- XGBoost
- Scikit-learn
- SHAP
- Sweetviz
- MLflow
- DVC
- DagsHub
- Streamlit
- Jupyter

---

## Data Availability

The underlying CDR datasets are not included in this public repository.

This is intentional because the project involves telecommunications data and the original datasets were provided as part of the Vanrise project.

The repository therefore provides the code, notebooks, project structure, and documentation necessary to understand the workflow without publishing the underlying data.

---

## Project Context

This work was conducted as part of a project originally provided by **Vanrise Solutions**.

The repository is intended to document the technical work performed by the author, including the implemented machine-learning pipeline, experiments, analysis, troubleshooting, and historical-pipeline investigation.