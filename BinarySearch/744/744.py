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

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        while target != 'z':
            target = chr(ord(target) + 1)
            index = self.BinarySearch(letters, target)
            if  index != -1:
                return letters[index]
        return letters[0]

        