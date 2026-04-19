#recursive function with memorization
from functools import cache


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# class Solution:
#     def climbStairs(self, n: int, memo = None) -> int:
#         if memo is None:
#             memo = {}
    
#         if n in memo:
#             return memo[n]
    
#         if n <= 1:
#             return 1
    
#         memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)

#         return memo[n]



# n: 0 1 2 3 4 ...
#    1 1 2 3 5
#Dynamic Programming
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         a, b = 1, 1
#         for _ in range(n - 1):
#             a, b = b, a + b
#         return b

