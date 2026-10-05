# DVC-Managed Datasets

This directory is reserved for datasets versioned during the machine-learning experiments using DVC.

The original project contains multiple versions of the train and test datasets corresponding to different experimental configurations.

## Expected structure

```text
dvc/
├── train_v1.parquet
├── train_v2.parquet
├── train_v3.parquet
├── train_v4.parquet
├── train_v5.parquet
├── test_v1.parquet
├── test_v2.parquet
├── test_v3.parquet
├── test_v4.parquet
└── test_v5.parquet
```

The versions correspond to different stages of dataset preparation, feature engineering, splitting, and experimentation.

## Public repository status

The Parquet datasets are intentionally excluded from the public repository.

If a DVC remote is configured for an authorized environment, the corresponding DVC metadata can be used to retrieve the datasets without storing them directly in Git.

The dataset-versioning workflow is documented in the dataset-versioning notebooks.