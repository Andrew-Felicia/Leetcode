from typing import List

class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            result = []
            for i in range(len(nums)):
                current = nums[i]
                remaining = nums[0:i] + nums[i + 1:]
                for elem in self.permute(remaining):
                    result.append([current] + elem)
            return result