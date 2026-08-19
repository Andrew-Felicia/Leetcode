
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans, left = 0, 0
        cur = 1
        for right, v in enumerate(nums):
            cur *= v

            while cur >= k:
                cur = cur // nums[left]
                left += 1
            ans += right - left + 1
        return ans