from sklearn.decomposition import PCA
import numpy as np


def log_transform(count):
  """Does logarithmic transform of matrix."""
  total = count.sum() if count.sum()!=0 else count.max()
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
  m = PCA(n_components=matrix[0].size-1)
  result = m.fit_transform(matrix)
  return result
