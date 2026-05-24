# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         m, n = len(board), len(board[0])
#         first = word[0]

#         #search the path in the board, if the path exists, return True, False otherwise.
#         def dfs(i, j, remaining_words):
#             if not remaining_words:
#                 return True

#             #up and down.
#             if i - 1 >= 0 and remaining_words[-1] == board[i - 1][j]:
#                 remaining_words.pop()
#                 return dfs(i - 1, j, remaining_words)
#             if i + 1 < m and remaining_words[-1] == board[i + 1][j]:
#                 remaining_words.pop()
#                 return dfs(i + 1, j, remaining_words)

#             #left and right.
#             if j - 1 >= 0 and remaining_words[-1] == board[i][j - 1]:
#                 remaining_words.pop()
#                 return dfs(i, j - 1, remaining_words)
#             if j + 1 < n and remaining_words[-1] == board[i][j + 1]:
#                 remaining_words.pop()
#                 return dfs(i, j + 1, remaining_words)





        
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == first:
#                     remaining_words = word[1:][::-1]
#                     if dfs(i, j, list(remaining_words)):
#                         return True
#         return False

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        if len(word) > m * n:
            return False

        from collections import Counter
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False

        # Optimization: If the word's ending character has a lower frequency 
        # in the board than its starting character, search the word backwards 
        # to dramatically reduce the search space branches.
        if board_counts[word[-1]] < board_counts[word[0]]:
            word = word[::-1]

        #search the path in the board, if the path exists, return True, False otherwise.
        def dfs(r, c, k):
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False
            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r - 1, c, k + 1) or \
            dfs(r + 1, c, k + 1) or \
            dfs(r, c - 1, k + 1) or \
            dfs(r, c + 1, k + 1))

            board[r][c] = temp
            
            return found
            

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False