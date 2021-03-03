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

Use this command to see PCA results of matrix:

```
implement_generate_pca()
```


### Running tests

Tests can be run using the following command:

```
pytest tests/test_log_transform_pca.py
```
