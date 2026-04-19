from typing import List

class Solution:
    def BinarySearch(self, nums, target):
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

    def searchInsert(self, nums: List[int], target: int) -> int:
        index = self.BinarySearch(nums, target)
        if index != -1:
            return index
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)