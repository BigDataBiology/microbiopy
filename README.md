# Microbiopy

Microbiopy is a tool that performs operations on sample input. Currently, it does the following:

1. [Filter Features](#Filter_Features): Filters features across samples based on minimum prevalence, minimum prevalence fraction, minimum average abundance, and minimum abundance fraction.

2. [Principal Component Analysis](#Principal_Component_Analysis): Performs principal component analysis on the data after executing a log transform on it. Reduces dimensionality of input data by 1 and gives the relevant relationship.

## Filter_Features
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


## Principal_Component_Analysis
### Input

Input Matrix.

Example:

```
res = do_pca(matrix)
```

### Output

PCA output, dimensionally reduced by one.

### Running tests

Tests can be run using the following command:

```
pytest tests/test_log_transform_pca.py
```
