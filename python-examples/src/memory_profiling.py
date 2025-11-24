"""
``memory_profiler`` provides line-by-line memory usage reports for functions decorated with @profile.
Execute this script with ``python -m memory_profiler src/memory_profiling.py``
"""

from memory_profiler import profile

@profile
def inefficient_processing(n):
    data = list(range(n))       
    squared = [x**2 for x in data]  
    cubed = [x**3 for x in data]
    return sum(squared) + sum(cubed)

@profile
def efficient_processing(n):
    return sum(x**2 for x in range(n)) + \
           sum(x**3 for x in range(n))

if __name__ == "__main__":
    n = 1_00_000 
    print("Running inefficient version...")
    result1 = inefficient_processing(n)
    print("Running efficient version...")
    result2 = efficient_processing(n)
    print(f"Both produce the same result? {result1 == result2}")