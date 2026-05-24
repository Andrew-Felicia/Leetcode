from typing import List

class Solution:
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = self.binarySearch(nums, target)
        if index == -1:
            return [-1, -1]

        # Expand left
        start = index
        while start > 0 and nums[start - 1] == target:
            start -= 1

        # Expand right
        end = index
        while end < len(nums) - 1 and nums[end + 1] == target:
            end += 1

        return [start, end]


