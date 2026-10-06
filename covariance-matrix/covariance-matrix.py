import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    x = np.asarray(X, dtype=float)
    mu = np.mean(x, axis=0)
    x_tilde = x - mu
    return np.dot(x_tilde.T, x_tilde)/(len(x) - 1)