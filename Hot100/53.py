# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
        
#         # Initialize the variables to the first element (or negative infinity for safety)
#         # We can use the first element since the constraints guarantee nums.length >= 1.
#         current_max = nums[0]  # Max sum of subarray ending at the current index
#         global_max = nums[0]   # Max sum found anywhere in the array
        
#         # Iterate from the second element
#         for i in range(1, len(nums)):
#             num = nums[i]
            
#             # Key Kadane's Step: 
#             # The new 'current_max' is EITHER the current number (starting a new subarray)
#             # OR the current number extending the previous subarray.
#             current_max = max(num, current_max + num)
            
#             # Update the global maximum sum found so far
#             global_max = max(global_max, current_max)
            
#         return global_max

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dp[i]=maximum subarray sum ending at i
        #throw it away
        # start over
        # That’s the whole algorithm.
        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            ans = max(ans, dp[i])
        return ans