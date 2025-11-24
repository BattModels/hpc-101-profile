"""
Py-spy is a sampling profiler for Python programs. 
It allows users to analyze the performance of a running Python application without modifying its code or restarting the program. 
This makes it particularly useful for debugging performance issues in production environments where minimal impact on the running application is crucial.
Execute this scipt with py-spy record --rate 1000 -o flamegraph.svg -- python -m src.flame_graph_example
"""

import numpy as np
import time


def compute_fibonacci(n):
    """Recursive Fibonacci."""
    if n <= 1:
        return n
    return compute_fibonacci(n - 1) + compute_fibonacci(n - 2)


def matrix_operations(size):
    """Perform various matrix operations."""
    # Matrix multiplication
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.dot(A, B)

    # Eigenvalue computation
    eigenvalues = np.linalg.eigvals(C)

    # SVD decomposition
    U, s, Vt = np.linalg.svd(C)

    return np.sum(eigenvalues)


def monte_carlo_pi(n_samples):
    """Estimate Pi using Monte Carlo method."""
    x = np.random.uniform(-1, 1, n_samples)
    y = np.random.uniform(-1, 1, n_samples)

    inside_circle = (x**2 + y**2) <= 1
    pi_estimate = 4 * np.sum(inside_circle) / n_samples

    return pi_estimate


def main():
    print("Starting profiling demo...")

    print("Matrix operations...")
    result1 = matrix_operations(200)
    print(f"   Result: {result1:.4f}")

    print("Monte Carlo Pi estimation...")
    result5 = monte_carlo_pi(1_000_000)
    print(f"   Pi estimate: {result5:.6f}")

    print("Fibonacci computation...")
    result6 = compute_fibonacci(34)
    print(f"   Result: {result6}")


if __name__ == "__main__":
    main()
