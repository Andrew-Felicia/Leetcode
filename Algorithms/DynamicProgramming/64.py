from typing import List
from functools import cache
#time limit exceeded
#tc: O(2^(m + n))
#sc: O(m + n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #return minimum path sum
        def minPathSumHelper(i, j):
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[i][j]
            else:
                return min(minPathSumHelper(i, j - 1), minPathSumHelper(i - 1, j)) + grid[i][j]
        return minPathSumHelper(len(grid) - 1, len(grid[0]) - 1)


#passed all the test after adding the decorator.
#tc: O(mn)
#sc: O(mn)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #return minimum path sum
        @cache
        def minPathSumHelper(i, j):
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[i][j]
            else:
                return min(minPathSumHelper(i, j - 1), minPathSumHelper(i - 1, j)) + grid[i][j]
        return minPathSumHelper(len(grid) - 1, len(grid[0]) - 1)



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1]) + x
        return f[m][n]