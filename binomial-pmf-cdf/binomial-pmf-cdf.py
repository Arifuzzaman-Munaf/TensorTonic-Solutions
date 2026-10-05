import math
def binomial_pmf(n: int, p: float, k: int):
    return math.comb(n, k) * math.pow(p, k) * math.pow(1-p, n-k)
    
def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    pmf = float(binomial_pmf(n, p, k))
    cdf = 0
    for i in range(k):
        cdf += binomial_pmf(n, p, i)
    
    return {
        "pmf" : pmf,
        "cdf" : cdf + pmf
    }