# Daily Profiles

This directory contains the primary daily MSISDN-level profiles generated from the CDR data.

The profiling process produces one behavioral profile per MSISDN for each day of the observation period.

## Expected structure

```text
profiles/
├── day_01.parquet
├── day_02.parquet
├── ...
├── day_15.parquet
└── all_profiles.parquet
```

The daily datasets correspond to the 15-day observation period used in the project.

`all_profiles.parquet` represents the combined profile dataset.

## Public repository status

The generated profile datasets have been removed because they are derived from the non-public CDR data.

The profiling methodology is preserved in the project notebooks.