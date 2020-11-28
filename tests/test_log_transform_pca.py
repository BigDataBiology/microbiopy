import numpy as np
from microbiopy import log_transform_pca as ltp


def test_log_transform_pca():
    """Tests the log_transform_pca function."""
    matrix = np.array([[1, 1], [2, 1], [3, 2],
                       [1, 1], [2, 1], [3, 2]], dtype=np.float32)
    lt_test = np.array([[0.04879012,  0.04879012], [0.71783978,  0.04879012],
                        [1.11514163, 0.71783978], [0.04879012, 0.04879012],
                        [0.71783978, 0.04879012], [1.11514163,  0.71783978]],
                       dtype=np.float32)

    assert np.allclose(ltp.log_transform(matrix), lt_test)

    pca_test = [[-0.60592264],
                [-0.0467416],
                [0.65266424],
                [-0.60592264],
                [-0.04674162],
                [0.65266424]]

    assert np.allclose(ltp.do_pca(matrix), pca_test)
