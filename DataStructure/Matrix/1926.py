# >>> s = [[False] * 5]
# >>> s
# [[False, False, False, False, False]]
# >>> s= [[False] * 5 for _ in range(5)]
# >>> s
# [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]

from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        vis = [[False] * n for _ in range(m)] #mark if it's visited
        sx, sy = entrance
        vis[sx][sy] = True
        ans = 1
        q = [(sx, sy)] #this store the coordinates which need to be visited in the same level.
        while q:
            tmp = q
            q = []
            for i, j in tmp:
                for x, y in (i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j):
                    if x >= 0 and x < m and y >= 0 and y < n and maze[x][y] == "." and not vis[x][y]:
                        if x == 0 or y == 0 or x == m - 1 or y == n - 1: #reach the exit.
                            return ans
                        q.append((x, y))
                        vis[x][y] = True
            ans += 1
        return -1




        