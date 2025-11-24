# python -m kernprof -l -v -m src.line_profiler_example

import numpy as np
from .matrix_multiply import matrix_multiply_naive

@profile  # This uses kernprof's injected profiler
def run_multiplication():
    """Wrapper function to profile the multiplication."""
    size = 200
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    result = matrix_multiply_naive(A, B)
    return result

if __name__ == "__main__":
    result = run_multiplication()