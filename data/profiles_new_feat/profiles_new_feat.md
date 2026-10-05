# Profiles — New Feature Version

This directory contains the alternative daily profile datasets generated during the later feature-engineering experiments.

These profiles correspond to the updated feature configuration explored in the later project iterations.

## Expected structure

```text
profiles_new_feat/
├── day_01.parquet
├── day_02.parquet
├── ...
├── day_15.parquet
└── all_profiles.parquet
```

These datasets were used by the later experimental pipeline and feature-engineering notebooks.

## Public repository status

The generated profile datasets have been removed from the public repository because they are derived from the non-public CDR data.

The corresponding methodology and experiments remain documented in the notebooks under:

```text
notebooks/#3_sgkf_rv_label_day_new_feats/
```