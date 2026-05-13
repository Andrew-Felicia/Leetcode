from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0: return 0


        minutes = 0
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):
                br, bc = queue.popleft()
                for r, c in directions:
                    ar, ac = br + r, bc + c
                    if 0 <= ar < m and 0 <= ac < n and grid[ar][ac] == 1:
                        grid[ar][ac] = 2
                        fresh_count -= 1
                        queue.append((ar, ac))

        return minutes if fresh_count == 0 else -1