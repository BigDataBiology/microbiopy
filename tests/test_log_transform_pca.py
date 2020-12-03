import numpy as np
from microbiopy import log_transform_pca as ltp


def test_log_transform_pca():
    """Tests the log_transform_pca function."""
    matrix = np.array([[1, 1], [2, 1], [3, 2],
                       [1, 6], [2, 5], [3, 4]], dtype=np.float32)
    lt_test = np.array([[0.03174867, 0.03174867],
                        [0.7091475, 0.03174867],
                        [1.1093075, 0.7091475],
                        [0.03174867, 1.7971214],
                        [0.7091475, 1.6158688],
                        [1.1093075, 1.3943266]],
                       dtype=np.float32)

    assert np.allclose(ltp.log_transform(matrix), lt_test)

    pca_test = np.array([[0.93256223,  0.5285643],
                         [0.89084977, -0.14754908],
                         [0.19009575, -0.50523734],
                         [-0.82946044, 0.6372711],
                         [-0.6902641, -0.05000322],
                         [-0.49378312, -0.46304584]],
                        dtype=np.float32)

    assert np.allclose(ltp.do_pca(matrix), pca_test)
