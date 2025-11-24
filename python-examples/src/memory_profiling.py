# python -m memory_profiler src/memory_profiling.py
from memory_profiler import profile

@profile
def inefficient_processing(n):
    data = list(range(n))       # Large allocation
    squared = [x**2 for x in data]  # Another copy!
    cubed = [x**3 for x in data]    # Yet another!
    return sum(squared) + sum(cubed)

@profile
def efficient_processing(n):
    # Generators - no intermediate storage
    return sum(x**2 for x in range(n)) + \
           sum(x**3 for x in range(n))

if __name__ == "__main__":
    n = 1_00_000 
    print("Running inefficient version...")
    result1 = inefficient_processing(n)
    print("\nRunning efficient version...")
    result2 = efficient_processing(n)
    print(f"\nBoth produce the same result: {result1 == result2}")