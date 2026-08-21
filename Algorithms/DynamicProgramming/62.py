#time limit exceed
# class Solution:
#     #return how many ways from (0,0) to (m - 1, n - 1)
#     def uniquePaths(self, m: int, n: int) -> int:
#         ans = 0
#         def helper(i, j):
#             nonlocal ans. #In Python, if you try to modify a variable (ans += 1) 
#             #that lives outside your inner function, Python thinks you are trying 
#             #to create a new local variable before declaring it.
#             if i >= m or j >= n:
#                 return
#             if i == m - 1 and j == n - 1:
#                 ans += 1
#                 return
#             else:
#                 return helper(i + 1, j) or helper(i, j + 1)

#         helper(0, 0)
#         return ans
        

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # A dictionary to remember coordinates we've already solved
        memo = {}

        def helper(i, j):
            # Base Case 1: Out of bounds (off the grid)
            if i >= m or j >= n:
                return 0
                
            # Base Case 2: Reached the destination
            if i == m - 1 and j == n - 1:
                return 1
            
            # If we already calculated the ways from (i, j), just return it
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Otherwise, calculate it: Go Down + Go Right
            memo[(i, j)] = helper(i + 1, j) + helper(i, j + 1)
            return memo[(i, j)]

        return helper(0, 0)


from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)