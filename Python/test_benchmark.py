import pytest
import numpy as np
import psutil
import os
from matrix_multiplication import matrix_multiplication


def generate_random_matrix(size):
    return np.random.randint(0, 10, (size, size)).tolist()

def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss / 1024


@pytest.mark.parametrize("size", [10,100,300,500,1000])
def test_basic_matrix_multiplication(benchmark, size):
    A = generate_random_matrix(size)
    B = generate_random_matrix(size)

    memory_before = get_memory_usage()

    result = benchmark.pedantic(matrix_multiplication,
                                args=(A, B),
                                rounds=1,
                                warmup_rounds=2,
                                iterations=5)

    memory_after = get_memory_usage()

    memory_used = memory_after - memory_before
    print(f"Memory used after benchmark {size}x{size}: {memory_used} KB")

    assert len(result) == size
    assert len(result[0]) == size

