import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    var = float(np.var(x, ddof=1))
    std = float(var ** 0.5)
    return {
        "variance" : var,
        "standard_deviation" : std
    }
    