# Principal Component Analysis

Performs principal component analysis on the data after executing a log transform on it. Reduces dimensionality of input data by 1 and gives the relevant relationship.

### Input

Input Matrix.

Example:

```
res = do_pca(matrix)
```

### Output

PCA output, dimensionally reduced to two. Use plot_pca(matrix) to see PCA results of matrix.

### Running tests

Tests can be run using the following command:

```
pytest tests/test_log_transform_pca.py
```
