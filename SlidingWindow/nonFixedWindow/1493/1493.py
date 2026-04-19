from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, left = 0, 0
        cur = 0
        for right, v in enumerate(nums):
            cur += 1 - nums[right] #count the number of 0's
            while cur > 1:
                cur -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left)
        return ans
