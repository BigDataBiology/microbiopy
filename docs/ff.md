# Filter Features

Filters features across samples based on minimum prevalence, minimum prevalence fraction, minimum average abundance, and minimum abundance fraction.

### Input

m * n Sample-by-Feature matrix and the filtering criteria.

Example:

```
res = filter_features(matrix, min_prevalence=2, min_prevalence_fraction=0.8)
```

### Output

Final numpy array filtered out using prevalence and abundance values (in that order).

### Running tests

Tests can be run using the following command:

```
pytest tests/test_filter_features.py
```
