import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    magnitude_a = np.linalg.norm(a, ord=2)
    magnitude_b = np.linalg.norm(b, ord=2)
    if magnitude_a and magnitude_b:
        return float(np.dot(a, b)/(magnitude_a * magnitude_b))
    return 0.0