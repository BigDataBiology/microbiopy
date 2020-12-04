from sklearn.decomposition import PCA
import numpy as np
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
    Reduces by one dimension.
    """
    matrix = np.asarray(matrix)
    matrix = log_transform(matrix)
    m = PCA(n_components=2)
    result = m.fit_transform(matrix)
    return result


def generate_pca(matrix):
    """
    Generates plot for PCA results.
    """
    y = np.arange(len(matrix))
    matrix = np.asarray(matrix)
    X_reduced = do_pca(matrix)
    plt.figure()
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='Accent')
    plt.xlabel('First PC')
    plt.ylabel('Second PC')
    plt.show()
