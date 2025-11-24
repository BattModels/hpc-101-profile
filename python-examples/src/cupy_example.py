import cupy as cp
from cupyx.profiler import benchmark
import time

def gpu_matmul():
    A = cp.random.randn(5000, 5000, dtype=cp.float32)
    B = cp.random.randn(5000, 5000, dtype=cp.float32)
    C = cp.matmul(A, B)
    return C

print(benchmark(gpu_matmul, n_repeat=10))