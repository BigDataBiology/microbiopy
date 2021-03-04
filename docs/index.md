# Microbiopy

Microbiopy is a tool that performs analysis on microbiome count data. Currently, it does the following:

1. **Filter Features**: Filters features across samples based on minimum prevalence, minimum prevalence fraction, minimum average abundance, and minimum abundance fraction.

2. **Principal Component Analysis**: Performs principal component analysis on the data after executing a log transform on it. Reduces dimensionality of input data to 2 and gives the relevant relationship via a Second PC versus First PC plot.
