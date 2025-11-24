"""
cProfile is a module within Python's standard library that provides a deterministic profiling tool for Python programs. 
It helps identify bottlenecks and areas of inefficiency in your Python code by showing where the program spends most of its time.

- ncalls: The number of times a function was called.
- tottime: The total time spent in a function, excluding time spent in sub-functions called by that function.
- percall (tottime): The average time per call for tottime.
- cumtime: The cumulative time spent in a function, including time spent in sub-functions called by that function.
- percall (cumtime): The average time per call for cumtime.
- filename:lineno(function): The location of the function in your code.

Execute this script with: python -m src.cProfile_example
"""

import cProfile
import pstats
import numpy as np

from .matrix_multiply import matrix_multiply_naive

size = 350

profiler = cProfile.Profile()
profiler.enable()
A = np.random.rand(size, size)
B = np.random.rand(size, size)
result = matrix_multiply_naive(A, B)
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumtime')  # Sort by cumulative time
stats.print_stats(10)        # Show top 10