from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_positive = []
        for i in nums:
            if i > 0:
                nums_positive.append(i)
        nums_positive = set(nums_positive)
        if not nums_positive:
            return 1

        maxValue = max(nums_positive)
        for i in range(1, maxValue):
            if i not in nums_positive:
                return i
        return maxValue + 1
    
# Problem 1 — remove() while iterating

# This is dangerous:

# for i in nums:
#     if i <= 0:
#         nums.remove(i)

# Because modifying a list while iterating can skip elements.

# Example:

# nums = [-1,-2,1]

# After removing -1:

# list shifts left

# and -2 may get skipped.