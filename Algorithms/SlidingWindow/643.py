#

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans, cur = float('-inf'), 0
        for i, v in enumerate(nums):
            cur += v

            left = i - k + 1
            if left < 0:
                continue
            
            if cur / k > ans:
                ans = cur / k
            
            cur -= nums[left]
        return ans