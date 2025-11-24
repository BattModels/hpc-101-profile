using CUDA
using BenchmarkTools

function gpu_vector_add!(c, a, b)
    i = (blockIdx().x - 1) * blockDim().x + threadIdx().x
    if i <= length(c)
        @inbounds c[i] = a[i] + b[i]
    end
    return nothing
end

function run_gpu_profiling(N=1_000_000_000)
    println("Creating arrays of size $N...")
    a = CUDA.ones(Float32, N)
    b = CUDA.ones(Float32, N)
    c = CUDA.zeros(Float32, N)
    
    threads = 256
    blocks = cld(N, threads)
    println("Kernel configuration: $blocks blocks × $threads threads")
    
    println("Compiling kernel (first run)...")
    @cuda threads=threads blocks=blocks gpu_vector_add!(c, a, b)
    CUDA.synchronize()
    
    println("=== Method 1: CUDA Events (most accurate GPU time) ===")
    start_event = CUDA.CuEvent()
    stop_event = CUDA.CuEvent()
    
    CUDA.record(start_event)
    @cuda threads=threads blocks=blocks gpu_vector_add!(c, a, b)
    CUDA.record(stop_event)
    CUDA.synchronize()
    
    gpu_time = CUDA.elapsed(start_event, stop_event)
    println("GPU kernel time: $(gpu_time) ms")
    println("Effective bandwidth: $(3 * N * sizeof(Float32) / gpu_time / 1e6) GB/s")
    
    println("=== Method 2: CUDA.@time ===")
    CUDA.@time @cuda threads=threads blocks=blocks gpu_vector_add!(c, a, b)
    
    println("=== Method 3: Manual timing with synchronization ===")
    CUDA.synchronize()
    t_start = time_ns()
    @cuda threads=threads blocks=blocks gpu_vector_add!(c, a, b)
    CUDA.synchronize()  
    t_end = time_ns()
    total_time = (t_end - t_start) / 1e6 
    println("Total time (launch + execute + sync): $(total_time) ms")
    
    println("=== Method 4: BenchmarkTools (statistical) ===")
    result = @benchmark begin
        @cuda threads=$threads blocks=$blocks gpu_vector_add!($c, $a, $b)
        CUDA.synchronize()
    end samples=100 seconds=30
    
    println("Minimum time: $(minimum(result.times) / 1e6) ms")
    println("Median time: $(median(result.times) / 1e6) ms")
    println("Mean time: $(mean(result.times) / 1e6) ms")
    
    # Calculate theoretical peak bandwidth
    data_moved = 3 * N * sizeof(Float32) / 1e9  # GB (read a, read b, write c)
    achieved_bandwidth = data_moved / (minimum(result.times) / 1e9)
    println("Data moved: $(data_moved) GB")
    println("Achieved bandwidth: $(achieved_bandwidth) GB/s")
    
    println("\nVerifying correctness:")
    sample = Array(c[1:10])
    println("First 10 elements: ", sample)
    println("All elements equal 2.0? ", all(sample .≈ 2.0f0))
    
    return
end