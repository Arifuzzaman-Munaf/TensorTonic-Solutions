import math
def get_pmf(lam: float, k: int):
    return ((lam ** k) * math.e **(-lam)) / math.factorial(k)
    
def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    cdf = 0
    for i in range(k):
        cdf += get_pmf(lam, i)
    pmf = get_pmf(lam, k)
    return {
        "pmf" : pmf,
        "cdf" : pmf + cdf
    }