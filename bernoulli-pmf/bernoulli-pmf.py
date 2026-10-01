import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x = np.asarray(x)
    pmf = np.pow(p, x) * np.pow(1 - p, 1 - x)
    mean = float(p)
    variance = float(p * (1 - p))
    return {
        "pmf" : pmf,
        "mean" : mean,
        "variance": variance
    }