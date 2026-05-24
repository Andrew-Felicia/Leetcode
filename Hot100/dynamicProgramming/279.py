class Solution:
    def numSquares(self, n: int) -> int:
        #dp[i] denote least number of perfect square numbers that sum to i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]

        for i in range(1, n + 1):
            for square in squares:
                if i - square >= 0:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]
    
#altenative solution
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        queue = deque([(n, 0)]) # (remaining_value, step_count)
        visited = {n}
        
        while queue:
            rem, steps = queue.popleft()
            
            for square in squares:
                target = rem - square
                if target == 0:
                    return steps + 1
                if target > 0 and target not in visited:
                    visited.add(target)
                    queue.append((target, steps + 1))
        return 0