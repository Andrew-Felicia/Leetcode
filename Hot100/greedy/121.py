# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 0 or len(prices) == 1:
#             return 0
#         result = []
#         for i in range(len(prices)):
#             for j in range(i + 1,len(prices)):
#                 if(prices[j] >= prices[i]):
#                     result.append(prices[j] - prices[i])
#                 else:
#                     result.append(0)
#         return max(result)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0

        minPrice = prices[0]
        profit = 0
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] > minPrice:
                profit = prices[i] - minPrice
                if profit > maxProfit:
                    maxProfit = profit
            if prices[i] < minPrice:
                minPrice = prices[i]
        return maxProfit