from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import filter_features as ff


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


def generate_pca(matrix, i):
    """
    Generates plot for PCA results.
    """

    y = np.arange(len(matrix))
    matrix = np.asarray(matrix)
    X_reduced = do_pca(matrix)
    print(X_reduced)
    mOTU_f = pd.DataFrame(X_reduced, columns=['PCA_1', 'PCA_2'], index=i)    # PCA DF

    meta = pd.read_csv('../tests/data/coelho2018metadata.tsv', sep ='\t', index_col=0)
    meta.index.names = [None]
    meta['S_No'] = meta.index

    mOTU_f.index.name = 'S_No'
    mOTU_f.reset_index(inplace=True)

    res = pd.merge(mOTU_f, meta, on="S_No", how="inner")
    x1 = res[res['PhenotypeShort']=='Lean']['PCA_1']
    y1 = res[res['PhenotypeShort']=='Lean']['PCA_2']

    x2 = res[res['PhenotypeShort']=='Overweight']['PCA_1']
    y2 = res[res['PhenotypeShort']=='Overweight']['PCA_2']

    plt.figure()
    plt.scatter(x1, y1, marker='o')
    plt.scatter(x2, y2, marker='^')
    plt.xlabel('First PC')
    plt.ylabel('Second PC')
    plt.legend(['Lean', 'Overweight'])
    plt.show()

mOTU = pd.read_table('../tests/data/mOTU_abundance_raw.tab', index_col=0)
mOTU = mOTU.transpose()
c = mOTU.columns
i = mOTU.index

x = ff.filter_features(mOTU, min_abundance_fraction=0.01)
generate_pca(x, i)
