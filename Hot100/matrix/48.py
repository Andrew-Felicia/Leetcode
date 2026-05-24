# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)

#         #Matrix Transpose
#         for i in range(n):
#             for j in range(i):
#                 tmp = matrix[i][j]
#                 matrix[i][j] = matrix[j][i]
#                 matrix[j][i] = tmp

#         #rotate rows of matrix
#         for i in range(n):
#             left, right = 0, n - 1
#             while left < right:
#                 tmp = matrix[i][left]
#                 matrix[i][left] = matrix[i][right]
#                 matrix[i][right] = tmp
#                 left += 1
#                 right -= 1

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 第一步：转置
        for i in range(n):
            for j in range(i):  # 遍历对角线下方元素
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第二步：行翻转
        for row in matrix:
            row.reverse()