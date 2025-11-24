# python -m src.cProfile_example
import pstats
import numpy as np

from .matrix_multiply import matrix_multiply_naive

size = 200
A = np.random.rand(size, size)
B = np.random.rand(size, size)

# Profile your code
profiler = cProfile.Profile()
profiler.enable()
result = matrix_multiply_naive(A, B)
profiler.disable()

# Analyze results
stats = pstats.Stats(profiler)
stats.sort_stats('cumtime')  # Sort by cumulative time
stats.print_stats(10)        # Show top 10