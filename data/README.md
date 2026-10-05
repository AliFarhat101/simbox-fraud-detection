# Data

This directory contains the datasets and data-derived artifacts used throughout the SIMBox fraud detection project.

The actual datasets are **not included in this public repository** because they originate from a non-public telecommunications dataset and contain data that is not intended for public distribution.

The directory structure is preserved to document the expected project organization and to allow the processing notebooks and pipelines to be reproduced in an authorized environment.

## Directory structure

```text
data/
├── raw_cdr/
├── profiles/
├── profiles_new_feat/
├── dvc/
└── results/
```

### `raw_cdr/`

Contains the raw and preprocessed CDR datasets used as inputs to the project.

### `profiles/`

Contains the daily MSISDN-level behavioral profiles generated from the CDR data.

### `profiles_new_feat/`

Contains the alternative profile datasets generated during the later feature-engineering experiments.

### `dvc/`

Reserved for versioned train/test datasets managed through DVC.

### `results/`

Contains data-derived model outputs and experiment artifacts.

## Data availability

The underlying CDR records, profiles, train/test datasets, predictions, and other data-derived files have been removed from the public repository.

The notebooks and project documentation preserve the processing methodology and expected data organization without distributing the underlying telecom data.