# Filter Features

Filters features across samples based on minimum prevalence, minimum prevalence fraction, minimum average abundance, and minimum abundance fraction.

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
