import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    X = np.asarray(X, dtype='float')
    # Write code here
    mask = np.isnan(X)

    if strategy == "mean":
        fill = np.nanmean(X, axis=0)
    else:
        fill = np.nanmedian(X, axis=0)
    fill = np.nan_to_num(fill, nan=0.0)
    return np.where(mask, fill, X)