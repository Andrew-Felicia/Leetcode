#

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, s = len(nums) + 1, 0
        left = 0
        for right, v in enumerate(nums):
            s += v
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right - left + 1)
        return ans if ans <= len(nums) else 0