import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    if np.linalg.det(A) == 0:
        return None

    A = np.asarray(A, dtype=float)
    n = len(A[0])
    I = np.eye(n)
    AI = np.hstack((A, I))

    for i in range(n):
        AI[i] = AI[i] / AI[i, i]

        for j in range(n):
            if i != j:
                AI[j] = AI[j] - AI[j, i] * AI[i]
    return AI[:, n:]