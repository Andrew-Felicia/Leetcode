# For the provided Quick Sort implementation:

# - **Best/average time:** \(O(n \log n)\)
# - **Worst-case time:** \(O(n^2)\), when partitions are repeatedly very unbalanced
# - **Space:** \(O(n \log n)\) on average for this specific implementation, because each recursion creates new lists
# - **Worst-case space:** \(O(n^2)\)

# A traditional **in-place Quick Sort** typically uses \(O(\log n)\) average auxiliary space for recursion, with \(O(n)\) in the worst case.

def quick_sort(values):
    if len(values) <= 1:
        return values

    pivot = values[len(values) // 2]
    smaller = [x for x in values if x < pivot]
    equal = [x for x in values if x == pivot]
    larger = [x for x in values if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


numbers = [8, 3, 1, 7, 0, 10, 2]
print(quick_sort(numbers))