# MICROBIOPY


import numpy as np


def filter_features(matrix, min_prevalence=0, min_prevalence_fraction=0.0,
                    min_average_abundance=0, min_abundance_fraction=0.0):

    """Filters features across samples based on argument.
    Input
    -----
    Sample-by-feature matrix.

    Arguments
    ---------
    min_prevalence(int): the minimum prevalence.
    min_prevalence_fraction(float): the minimum prevalence fraction.
    min_average_abundance(float): the minimum abundance.
    min_abundance_fraction(float): the minimum abundance fraction.

    Output
    ------
    A matrix of all features that pass the filter.
    """

    matrix = np.asarray(matrix, dtype=np.float32)

    (m, n) = matrix.shape

    if min_prevalence_fraction:
        min_prevalence = max(min_prevalence,
                             np.ceil(min_prevalence_fraction * m))

    keep = np.ones(n, bool)

    if min_prevalence:
        boolmatrix = (matrix > 0)
        prev = np.sum(boolmatrix, axis=0)
        keep &= (prev >= min_prevalence)

    if min_average_abundance or min_abundance_fraction:
        csum = np.sum(matrix, axis=0)

        if min_average_abundance:
            avg = csum/n
            keep &= (avg >= min_average_abundance)

        if min_abundance_fraction:
            total_sum = np.sum(matrix)
            fraction = csum/total_sum
            keep &= (fraction >= min_abundance_fraction)

    return matrix*keep
