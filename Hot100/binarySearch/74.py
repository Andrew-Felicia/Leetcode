# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
#         left, right = -1, m * n
        
        
#         while left + 1 < right:
#             mid = (left + right) // 2
#             x = matrix[mid // n][mid % n]
#             if x == target:
#                 return True
#             if x < target:
#                 left = mid
#             else:
#                 right = mid
#         return False

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False