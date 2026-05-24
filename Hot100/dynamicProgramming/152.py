from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]

            tmpMax = max(num, num * curMax, num * curMin)
            tmpMin = min(num, num * curMax, num * curMin)

            curMax = tmpMax
            curMin = tmpMin
            ans = max(ans, curMax)
        return ans