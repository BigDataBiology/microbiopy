# Microbiopy

Microbiopy is a tool that performs operations on sample input. Currently, it does the following:

1. [Filter Features](#Filter_Features): Filters features across samples based on minimum prevalence, minimum prevalence fraction, minimum average abundance, and minimum abundance fraction.

2. [Principal Component Analysis](#Principal_Component_Analysis): Performs principal component analysis on the data after executing a log transform on it. Reduces dimensionality of input data to 2 and gives the relevant relationshp via a Second PC versus First PC plot.

## Filter_Features
### Input

m * n Sample-by-Feature matrix and the filtering arguments:

**Arguments:**
- min_prevalence(int): the minimum prevalence.
- min_prevalence_fraction(float): the minimum prevalence fraction.
- min_average_abundance(float): the minimum abundance.
- min_abundance_fraction(float): the minimum abundance fraction.


Example:

```
res = filter_features(matrix, min_prevalence=1, min_prevalence_fraction=0.9,
                      min_average_abundance=18, min_abundance_fraction=0.5)
```


### Output

Final numpy array filtered out using prevalence and abundance values (in that order).

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

PCA output, dimensionally reduced to two. 


### PCA Plots

Use generate_pca method (with relevant arguments described below) to see PCA results of matrix:

**Arguments:**
- matrix: Abundance/prevalence values matrix
- i: Column labels of matrix
- meta: Metadata file
- marker_attribute: Attribute used to define markers in plot
- marker_value1: First value of marker attribute
- marker_value2: Second value of marker attribute
- join_on: Common column to join matrix and meta on

### Running tests

Tests can be run using the following command:

```
pytest tests/test_log_transform_pca.py
```

# Demonstration

View the [microbiopy demonstration](https://github.com/BigDataBiology/microbiopy_demo).
