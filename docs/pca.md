# Principal Component Analysis

Performs principal component analysis on the data after executing a log transform on it.


### Input

Input Matrix.

Example:

```
res = do_pca(matrix)
```

### Output

PCA output, dimensionally reduced to two. 


### PCA Plots

Use generate_pca method (with relevant arguments described below) to see PCA results of matrix:

**Arguments:**
- matrix: Abundance/prevalence values matrix
- i: Column labels in matrix
- meta: Metadata file
- marker_attribute: Attribute used to define markers in plot
- marker_value1: First value of marker attribute
- marker_value2: Second value of marker attribute
- join_on: Common column to join matrix and meta on

For more information, view the [microbiopy demonstration](https://github.com/BigDataBiology/microbiopy_demo)


### Running tests

Tests can be run using the following command:

```
pytest tests/test_log_transform_pca.py
```
