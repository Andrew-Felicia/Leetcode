from typing import List

# class Solution:
#     def BinarySearch(self, nums, target):
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1

#     def maximumCount(self, nums: List[int]) -> int:

# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         neg = pos = 0
#         for x in nums:
#             if x < 0:
#                 neg += 1
#             elif x > 0:
#                 pos += 1
#         return max(neg, pos)

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        import bisect
        
        # Find first index where nums[i] >= 0
        first_zero_or_positive = bisect.bisect_left(nums, 0)
        # Find first index where nums[i] > 0
        first_positive = bisect.bisect_right(nums, 0)
        
        neg = first_zero_or_positive          # count of negatives
        pos = len(nums) - first_positive      # count of positives
        
        return max(neg, pos)
