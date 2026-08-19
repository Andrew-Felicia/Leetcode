from typing import List

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         nums.sort()
#         #dp[i] denotes the sum to nums[i]
#         dp = [0] * (len(nums) + 1)
#         dp[0] = 0
#         for i in range(len(nums) - 1):
#             dp[i + 1] = dp[i] + nums[i]
#             if dp[i + 1] == sum(nums[i + 1:]):
#                 return True
#         return False
#it will not work with this case: [2,2,1,1]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        #dp[i] denote if it's possible to sum to i using numbers in nums.
        dp = [False] * (target + 1)
        dp[0] = True #choose nothing

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]