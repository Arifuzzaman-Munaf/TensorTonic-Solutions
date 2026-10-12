import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    x_bar = X - np.mean(X, axis=0)
    variance = (x_bar.T @ x_bar)/(len(X) - 1)
    std = np.sqrt(np.diag(variance))
    std_matrix = np.outer(std, std)
    return np.where(std_matrix != 0, variance/std_matrix, np.nan)