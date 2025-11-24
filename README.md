# HPC 101: Profiling

Demo repository for an introduction to HPC lesson on profiling.

## Overview

This repository contains practical examples and demonstrations for learning about profiling techniques in high-performance computing (HPC) applications. The examples are designed to help you understand how to identify performance bottlenecks, analyze code efficiency, and optimize computational workloads.

## Repository Structure

- **python-examples/**: Python profiling demonstrations
- **JuliaExamples/**: Julia profiling demonstrations

## Topics Covered

- CPU profiling and performance analysis
- CUDA kernel time and memory profiling
- Identifying computational bottlenecks

## Getting Started

1. Clone the repository
2. For CUDA examples `module load cuda/12.8.1`
   
### Python

3. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
4. `cd python-examples`
5. `uv sync`
   

### Julia

6. Install or load Julia `module load julia`
7. `cd JuliaExamples`
8. `]` to go to `Pkg` mode
9. `instantiate`

