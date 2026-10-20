import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x_bar = np.mean(x)
    standard_error = np.std(x, ddof=1) / (len(x) ** 0.5) 
    return float((x_bar - mu0) / standard_error)
    