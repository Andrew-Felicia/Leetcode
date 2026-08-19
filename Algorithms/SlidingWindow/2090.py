#
from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        cur = 0

        for i,v in enumerate(nums):
            cur += v
            if i < 2 * k:
                continue
            ans[i - k] = cur // (2 * k + 1)

            cur -= nums[i - 2 * k]
        return ans