# Filter Features

Filters features across samples based on minimum prevalence, minimum prevalence fraction, minimum average abundance, and minimum abundance fraction.

### Input

m * n Sample-by-Feature matrix and the filtering criteria.

Example:

```
res = filter_features(matrix, min_prevalence=2, min_prevalence_fraction=0.8)
```

### Output

A tuple of two m * n matrices (based on absolute and fractional filters) containing only those features that pass the filters.

### Running tests

Tests can be run using the following command:

```
pytest tests/test_filter_features.py
```
