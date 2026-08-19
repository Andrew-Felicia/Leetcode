# 70. Climbing Stairs
# 已解答
# 简单
# 相关标签
# conpanies icon
# 相关企业
# 提示
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 1
#         elif n == 1:
#             return 1
#         else:
#             return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution:
    def climbStairs(self, n: int, memo = None) -> int:
        if memo is None:
            memo = {}
    
        if n in memo:
            return memo[n]
    
        if n <= 1:
            return 1
    
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)

        return memo[n]

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # dp f[i]=f[i-1]+f[i-2]
#         f=[[] for _ in range(n+2)]
#         f[0],f[1]=1,1
#         for i in range(n):
#             f[i+2]=f[i+1]+f[i]
#         return f[n]
