# Model Results

This directory is reserved for model outputs and data-derived results generated during the SIMBox fraud detection experiments.

## Expected contents

The original project contains artifacts such as:

```text
best_xgb_params.json
best_xgb_params_v5.json
feature_importance_v5.csv
oof_predictions_v3.parquet
predictions_test_v3.parquet
```

These represent model parameters, feature-analysis outputs, and prediction datasets generated during different stages of the project.

## Public repository status

The original result files have been removed from the public repository.

In particular, prediction datasets are not distributed because they are derived from the underlying non-public data.

The methodology for generating these artifacts is preserved in the training, tuning, and evaluation notebooks.