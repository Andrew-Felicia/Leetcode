# Complexities:
# - Time: \(O(n \log n)\) in the best, average, and worst cases
# - Auxiliary space: \(O(n)\)
# - Recursion stack: \(O(\log n)\)
# - Stable: Yes


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # <= preserves the order of equal elements,
        # making the algorithm stable.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


numbers = [8, 3, 1, 7, 3, 10, 2]
numbers = merge_sort(numbers)
print(numbers)