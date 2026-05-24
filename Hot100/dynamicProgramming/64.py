#time limit exceeded
#tc: O(2^(m + n))
#sc: O(m + n)
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         #return minimum path sum
#         def minPathSumHelper(i, j):
#             if i < 0 or j < 0:
#                 return float('inf')
#             if i == 0 and j == 0:
#                 return grid[i][j]
#             else:
#                 return min(minPathSumHelper(i, j - 1), minPathSumHelper(i - 1, j)) + grid[i][j]
#         return minPathSumHelper(len(grid) - 1, len(grid[0]) - 1)


#passed all the test after adding the decorator.
#tc: O(mn)
#sc: O(mn)
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         #return minimum path sum
#         @cache
#         def minPathSumHelper(i, j):
#             if i < 0 or j < 0:
#                 return float('inf')
#             if i == 0 and j == 0:
#                 return grid[i][j]
#             else:
#                 return min(minPathSumHelper(i, j - 1), minPathSumHelper(i - 1, j)) + grid[i][j]
#         return minPathSumHelper(len(grid) - 1, len(grid[0]) - 1)