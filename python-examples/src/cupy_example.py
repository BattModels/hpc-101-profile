"""
CUDA kernel profiling with CuPy for GPU-accelerated computing.
Execution on the GPU is asynchronous: the Python interpreter immediately takes back control of the program execution, while the GPU is still executing the task. 
Conveniently, cupyx provides the function benchmark() that measures the actual execution time in the GPU.
Execute with: python -m src.cupy_example
"""
import cupy as cp
from cupyx.profiler import benchmark
import time

def gpu_matmul():
    A = cp.random.randn(5000, 5000, dtype=cp.float32)
    B = cp.random.randn(5000, 5000, dtype=cp.float32)
    C = cp.matmul(A, B)
    return C

print(benchmark(gpu_matmul, n_repeat=10))