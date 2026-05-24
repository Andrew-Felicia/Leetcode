from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        steps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            farthest = max(farthest, nums[i] + i)

            if i == current_end:
                steps += 1
                current_end = farthest
                if current_end >= len(nums) - 1:
                    break
        return steps