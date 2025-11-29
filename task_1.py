import random
import timeit

from insertion_sort import InsertionSort
from merge_sort import MergeSort


def benchmark_algorithm(label, func, data, runs):
    """Return total seconds to sort copies of data runs times."""
    timer = timeit.Timer(lambda: func(list(data)))
    return timer.timeit(number=runs)


def run_benchmarks():
    sizes = [1_000, 10_000, 20_000]

    runs = 3
    algorithms = {
        "Timsort (sorted)": sorted,
        "Merge sort": MergeSort.sort,
        "Insertion sort": InsertionSort.sort,
    }

    random.seed(100)
    results = []

    for size in sizes:
        data = [random.randint(0, size * 10) for _ in range(size)]
        for label, func in algorithms.items():
            elapsed = benchmark_algorithm(label, func, data, runs)
            results.append((label, size, elapsed))
    return results


def print_results(results):
    print("Empirical timing of sorting algorithms")
    print(f"{'Algorithm':<18} {'Size':>6} {'Seconds (total over runs)':>28}")
    for label, size, elapsed in results:
        print(f"{label:<18} {size:>6} {elapsed:>28.6f}")


if __name__ == "__main__":
    results = run_benchmarks()
    print_results(results)
