# goit-algo-hw-04

Benchmarking script comparing three sorting implementations (Python's Timsort via `sorted`, a custom merge sort, and insertion sort) on randomly generated integer arrays of varying sizes.

```
Empirical timing of sorting algorithms
Algorithm            Size    Seconds (total over runs)
Timsort (sorted)     1000                     0.000207
Merge sort           1000                     0.003478
Insertion sort       1000                     0.038936
Timsort (sorted)    10000                     0.002929
Merge sort          10000                     0.045659
Insertion sort      10000                     4.040453
Timsort (sorted)    20000                     0.006248
Merge sort          20000                     0.092861
Insertion sort      20000                    15.526919
```

## Conclusions
- Timsort (Python's built-in `sorted`) is the clear winner: about 0.006 seconds total for three runs on 20,000 items.
- Merge sort is slower than Timsort but still scales well (n log n): roughly 0.093 seconds on 20000 items.
- Insertion sort slows down rapidly as data grows: ~0.039 seconds at 1000 items, ~4 seconds at 10000, and ~15.5 seconds at 20000.
- For medium and large inputs, stick to Timsort or merge sort; insertion sort only makes sense for very small lists or as a helper step inside Timsort.

## Code references
- Benchmark runner and output: `task_1.py` (uses `merge_sort.py` and `insertion_sort.py`).
