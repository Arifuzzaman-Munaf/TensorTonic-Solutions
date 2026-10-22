import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    x = np.asarray(X, dtype=float)
    x_c = x - x.mean(axis=axis, keepdims=True)
    std_x = x.std(axis=axis, keepdims=True)
    return np.divide(x_c, std_x, out=np.zeros_like(x), where=std_x > eps)