# Alright, let’s build this from scratch slowly.

# ---

# Suppose:

# ```python id="jodw8t"
# coins = [1,2,5]
# amount = 11
# ```

# We want:

# ```text id="g8os5m"
# minimum number of coins to make 11
# ```

# Answer:

# ```text id="5g50d5"
# 5 + 5 + 1 = 3 coins
# ```

# ---

# # First thought (brute force)

# For 11, we could try:

# ```text id="9kqarf"
# take 1
# take 2
# take 5
# ```

# and continue recursively.

# But this repeats the same work many times.

# Example:

# ```text id="e8cv0y"
# to solve 11
# we need solve 10, 9, 6

# to solve 10
# we again solve 9, 8, 5
# ```

# Notice:

# ```text id="mga9e8"
# 9 gets solved repeatedly
# ```

# Dynamic Programming avoids recomputing.

# ---

# # The BIG IDEA

# Instead of directly solving 11:

# We solve:

# ```text id="e4p1zt"
# 0
# 1
# 2
# 3
# 4
# ...
# 11
# ```

# one by one.

# ---

# # Define dp

# We create an array:

# ```python id="ng6vyo"
# dp = ?
# ```

# Meaning:

# ```text id="1djlwm"
# dp[i] =
# minimum coins needed to make amount i
# ```

# Example:

# ```text id="4m5zmr"
# dp[3] = 2
# ```

# because:

# ```text id="me9a0k"
# 3 = 1 + 2
# ```

# 2 coins.

# ---

# # Step 1: initialize

# We need:

# ```python id="9ib4zl"
# dp[0] = 0
# ```

# Why?

# Because:

# ```text id="qvtghp"
# amount 0 needs 0 coins
# ```

# Then:

# ```python id="m2drfw"
# dp = [0, inf, inf, inf, inf, ...]
# ```

# `inf` means:

# ```text id="v6pobd"
# currently impossible / unknown
# ```

# ---

# # Now solve amounts one by one

# ---

# # Amount = 1

# Can we make 1?

# Try every coin.

# ---

# Using coin 1:

# ```text id="r4mk8z"
# 1 - 1 = 0
# ```

# We already know:

# ```text id="3hkrb5"
# dp[0] = 0
# ```

# So:

# ```text id="jlwmn7"
# make 0 using 0 coins
# then add one coin(1)
# ```

# Total:

# ```text id="9p13m2"
# 1 coin
# ```

# So:

# ```python id="uqeq5f"
# dp[1] = 1
# ```

# Now:

# ```python id="m9xnrw"
# dp = [0,1,inf,inf,inf...]
# ```

# ---

# # Amount = 2

# Try every coin.

# ---

# Using coin 1:

# ```text id="3tx4vq"
# 2 - 1 = 1
# ```

# We know:

# ```text id="n4bg0n"
# dp[1] = 1
# ```

# So:

# ```text id="ywsxzc"
# 1 existing coin + this new 1 coin
# = 2 coins
# ```

# Candidate:

# ```text id="jz4b7t"
# 2
# ```

# ---

# Using coin 2:

# ```text id="cc1jlwm"
# 2 - 2 = 0
# ```

# We know:

# ```text id="u11nh2"
# dp[0] = 0
# ```

# Add this coin:

# ```text id="3m1s61"
# 0 + 1 = 1 coin
# ```

# Better!

# So:

# ```python id="x5brpa"
# dp[2] = 1
# ```

# Now:

# ```python id="qhqjlwm"
# dp = [0,1,1,inf,inf...]
# ```

# ---

# # Amount = 3

# Try coin 1:

# ```text id="4dxrc0"
# 3 - 1 = 2
# ```

# ```text id="1mjlwm"
# dp[2] = 1
# ```

# Add current coin:

# ```text id="bpx9et"
# 1 + 1 = 2
# ```

# Candidate = 2.

# ---

# Try coin 2:

# ```text id="2om43x"
# 3 - 2 = 1
# ```

# ```text id="58igel"
# dp[1] = 1
# ```

# Add one coin:

# ```text id="fjlwmg"
# 1 + 1 = 2
# ```

# Still 2.

# ---

# Try coin 5:

# Cannot.

# So:

# ```python id="0ympg8"
# dp[3] = 2
# ```

# ---

# # Pattern emerges

# For every amount:

# ```text id="3ptz4d"
# try all coins
# ```

# Ask:

# ```text id="84vmce"
# if I use this coin,
# what smaller problem remains?
# ```

# That smaller problem is:

# ```text id="eztjlwm"
# dp[i - coin]
# ```

# Then:

# ```text id="wsvv8z"
# +1 because we used one coin now
# ```

# So formula becomes:

# dp[i]=\min(dp[i],\ dp[i-coin]+1)

# ---

# # Final code

# Now the code should make more sense:

# ```python id="q38l9x"
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         dp = [float('inf')] * (amount + 1)

#         dp[0] = 0

#         for i in range(1, amount + 1):

#             for coin in coins:

#                 if i - coin >= 0:

#                     dp[i] = min(
#                         dp[i],
#                         dp[i - coin] + 1
#                     )

#         if dp[amount] == float('inf'):
#             return -1

#         return dp[amount]
# ```

# ---

# # Most important mindset

# DP is usually:

# ```text id="n0stjv"
# big problem
# =
# smaller solved problems
# ```

# Here:

# ```text id="u1qtqg"
# amount 11
# depends on
# amount 10, 9, 6
# ```

# That is the core idea.


from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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