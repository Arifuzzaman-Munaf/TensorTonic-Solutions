import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    matrix = np.asarray(matrix, dtype = float)
    if np.allclose(matrix, matrix.T):
        eigenvalues = np.linalg.eigh(matrix)[0]
    else:
        eigenvalues = np.linalg.eig(matrix)[0].real
    return np.sort(eigenvalues)
    