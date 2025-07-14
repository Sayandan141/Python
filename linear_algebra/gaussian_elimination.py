"""
| Gaussian elimination method for solving a system of linear equations.
| Gaussian elimination - https://en.wikipedia.org/wiki/Gaussian_elimination
"""

import numpy as np

def gaussian_elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solves a system of linear equations using Gaussian elimination.
    
    Args:
        A: Square matrix of coefficients (n x n)
        b: Vector of constants (n x 1)
        
    Returns:
        Solution vector x where Ax = b
        
    Examples:
        >>> gaussian_elimination(np.array([[1, -4, -2], [5, 2, -2], [1, -1, 0]]), np.array([[-2], [-3], [4]]))
        array([[ 2.3 ],
               [-1.7 ],
               [ 5.55]])
        >>> gaussian_elimination(np.array([[1, 2], [5, 2]]), np.array([[5], [5]]))
        array([[0. ],
               [2.5]])
    """
    # Check if A is square
    if A.shape[0] != A.shape[1]:
        return np.array([])
    
    # Create augmented matrix [A|b]
    augmented = np.hstack((A.astype(float), b.astype(float)))
    n = A.shape[0]
    
    # Forward elimination
    for i in range(n):
        pivot = augmented[i, i]
        for j in range(i + 1, n):
            factor = augmented[j, i] / pivot
            augmented[j] -= factor * augmented[i]
    
    # Back substitution
    x = np.zeros((n, 1))
    for i in range(n-1, -1, -1):
        x[i] = (augmented[i, -1] - np.dot(augmented[i, i+1:n], x[i+1:])) / augmented[i, i]
    
    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()
