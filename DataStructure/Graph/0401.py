from collections import deque
from typing import List

class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        adjcency = [[] for _ in range(n)]
        for from_node, to_node in graph:
            adjcency[from_node].append(to_node)

        #BFS
        queue = deque([start])

        visited = [False] * n
        visited[start] = True

        while queue:
            cur = queue.popleft()

            if cur == target:
                return True
            for neighbor in adjcency[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return False