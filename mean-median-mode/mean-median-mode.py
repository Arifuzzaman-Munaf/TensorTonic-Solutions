from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean = float(np.mean(x))
    median = float(np.median(x))
    vals, counts = np.unique(x, return_counts=True)
    mode = float(vals[np.argmax(counts)])
    # Write code here
    return {
        "mean"   : mean,
        "median" : median,
        "mode"   : mode
    }