## Input

A sample-by-feature matrix.

## Arguments

min_prevalence(int): the minimum prevalence.
min_prevalence_fraction(float): the minimum prevalence fraction.
min_abundance(int): the minimum abundance.
min_abundance_fraction(float): the minimum abundance fraction.

Example:

```
res = filter_features(matrix, min_prevalence=2, min_prevalence_fraction=0.8)
```

## Running tests

Tests can be run using the following command:

```
pytest tests/test_filter_features.py
```
