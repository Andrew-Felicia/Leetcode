from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()

        left = 0
        ans = float('inf')
        n = len(nums)
        for right, v in enumerate(nums):
            
            while nums[right] > k * nums[left]:
                left += 1
            
            ans = min(ans, n - (right - left + 1))
        return ans