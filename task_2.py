from merge_sort import MergeSort


def merge_k_lists(sorted_lists):
    if not sorted_lists:
        return []

    merged = list(sorted_lists[0])
    for lst in sorted_lists[1:]:
        merged = MergeSort.merge(merged, lst)
    return merged


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Sorted list:", merged_list)
