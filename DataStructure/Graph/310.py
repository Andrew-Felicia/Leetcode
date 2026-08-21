from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        gragh = [set() for _ in range(n)]
        for u, v in edges:
            gragh[u].add(v)
            gragh[v].add(u)

        leaves = deque([i for i in range(n) if len(gragh[i]) == 1])

        remaining_leaves = n
        while remaining_leaves > 2:
            leaves_count = len(leaves)
            remaining_leaves -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                neighbor = gragh[leaf].pop()

                gragh[neighbor].remove(leaf)
                if len(gragh[neighbor]) == 1:
                    leaves.append(neighbor)
        return list(leaves) 