from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solution = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        pos_diago = set()
        neg_diago = set()

        def backTrack(row):
            if row == n:
                solution.append([''.join(r) for r in board])
            for col in range(n):
                if col in cols or (row + col) in pos_diago or (row - col) in neg_diago:
                    continue
                
                board[row][col] = "Q"
                cols.add(col)
                pos_diago.add(row + col)
                neg_diago.add(row - col)

                backTrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                pos_diago.remove(row + col)
                neg_diago.remove(row - col)




        backTrack(0)
        return solution
        