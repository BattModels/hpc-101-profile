# julia --track-allocation=user mem_profiling.jl

function allocating_version(n)
    A = rand(n, n)
    B = rand(n, n)
    C = A + B      # Allocates
    D = C * 2      # Allocates again
    return sum(D)
end

function efficient_version(n)
    A = rand(n, n)
    B = rand(n, n)
    C = similar(A)
    C .= A .+ B    # In-place with broadcasting
    C .*= 2        # In-place
    return sum(C)
end

@time allocating_version(1000) 
@time efficient_version(1000) 