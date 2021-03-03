from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def log_transform(count):
    """Does logarithmic transform of matrix."""
    count = np.asarray(count)
    total = count.sum() if (count.sum() != 0) else count.max()
    normalization = count / total
    pc = normalization[normalization > 0].min()
    normalization += pc
    count = count + pc
    lt_count = np.log(count)

    return lt_count


def do_pca(matrix):
    """
    Performs Principal Component Analysis on the matrix.
    """
    matrix = np.asarray(matrix)
    matrix = log_transform(matrix)
    m = PCA(n_components=2)
    result = m.fit_transform(matrix)
    return result


def generate_pca(matrix, i, meta, marker_attribute, marker_value1,
                 marker_value2, join_on):
    """
    Generates plot for PCA results.

    Arguments:
    ----------
    matrix: Abundance/prevalence values matrix
    i: Number of columns in matrix
    meta: Metadata file
    marker_attribute: Attribute used to define markers in plot
    marker_value1: First value of marker attribute
    marker_value2: Second value of marker attribute
    join_on: Common column to join matrix and meta on
    """

    matrix = np.asarray(matrix)
    X_reduced = do_pca(matrix)

    mOTU_f = pd.DataFrame(X_reduced,
                          columns=['PCA_1', 'PCA_2'], index=i)

    meta.index.names = [None]
    meta[join_on] = meta.index

    mOTU_f.index.name = join_on
    mOTU_f.reset_index(inplace=True)

    res = pd.merge(mOTU_f, meta, on=join_on, how="inner")

    x1 = res[res[marker_attribute] == marker_value1]['PCA_1']
    y1 = res[res[marker_attribute] == marker_value1]['PCA_2']

    x2 = res[res[marker_attribute] == marker_value2]['PCA_1']
    y2 = res[res[marker_attribute] == marker_value2]['PCA_2']

    plt.figure()
    plt.scatter(x1, y1, marker='o')
    plt.scatter(x2, y2, marker='^')
    plt.xlabel('First PC')
    plt.ylabel('Second PC')
    plt.legend([marker_value1, marker_value2])
    plt.show()
