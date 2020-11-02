import os
from microbiopy import filter_features as ff

def test_filter_features():
	matrix = [[19, 20, 21], [0, 17, 18], [0, 20, 15]]
	assert ff.filter_features(matrix, min_prevalence=2, min_prevalence_fraction=0.8) == ([[0, 20, 21], [0, 17, 18], [0, 20, 15]], [[0, 20, 21], [0, 17, 18], [0, 20, 15]])
	assert ff.filter_features(matrix, min_abundance=57, min_abundance_fraction=0.4) == ([[0, 20, 0], [0, 17, 0], [0, 20, 0]], [[0, 20, 21], [0, 17, 18], [0, 20, 15]])
