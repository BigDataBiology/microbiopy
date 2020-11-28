import numpy as np

from microbiopy import filter_features as ff


def test_filter_features():
    """Tests the filter_features function."""
    matrix = [[19, 20, 21], [0, 17, 50], [0, 20, 15]]
    x = [[0, 20, 21],
         [0, 17, 50],
         [0, 20, 15]]
    y = [[0,  0, 21],
         [0,  0, 50],
         [0,  0, 15]]
    z = [[0,  0, 21],
         [0,  0, 50],
         [0,  0, 15]]

    assert np.allclose(ff.filter_features(
        matrix, min_prevalence=2, min_prevalence_fraction=0.5), x)
    assert np.allclose(ff.filter_features(
        matrix, min_average_abundance=18, min_abundance_fraction=0.4), y)
    assert np.allclose(ff.filter_features(
        matrix, min_prevalence=1, min_prevalence_fraction=0.9,
        min_average_abundance=18, min_abundance_fraction=0.5), z)
