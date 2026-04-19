# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         ans = []
#         def rec(cost, i, cur):
#             cur += cost[i]
#             if i == len(cost) - 1 or i == len(cost) - 2:
#                 ans.append(cur)
#                 return
#             else:
#                 return rec(cost, i + 1, cur) or rec(cost, i + 2, cur)
        
#         rec(cost, 0, 0)
#         rec(cost, 1, 0)
#         return min(ans)


#超出内存限制
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def rec(i, cur):
#             cur += cost[i]
#             if i == len(cost) - 1 or i == len(cost) - 2:
#                 return [cur]
#             else:
#                 return rec(i + 1, cur) + rec(i + 2, cur)
        
        
#         return min(rec(0, 0) + rec(1, 0))


class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
# 上述代码的时间复杂度和空间复杂度都是 O(n)。注意到当 i≥2 时，dp[i] 只和 dp[i−1] 与 dp[i−2] 有关，
#因此可以使用滚动数组的思想，将空间复杂度优化到 O(1)。


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         prev = curr = 0
#         for i in range(2, n + 1):
#             nxt = min(curr + cost[i - 1], prev + cost[i - 2])
#             prev, curr = curr, nxt
#         return curr