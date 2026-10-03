
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] means the minimum coins to sum up to i.
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] < float('inf') else -1
    

#altenative solution
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        queue = deque([(0, 0)]) # (current_sum, num_coins)
        visited = {0}
        
        while queue:
            curr_sum, count = queue.popleft()
            
            for coin in coins:
                next_sum = curr_sum + coin
                
                if next_sum == amount:
                    return count + 1
                
                if next_sum < amount and next_sum not in visited:
                    visited.add(next_sum)
                    queue.append((next_sum, count + 1))
                    
        return -1