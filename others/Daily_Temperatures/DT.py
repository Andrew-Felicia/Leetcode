# 739. Daily Temperatures
# 已解答
# 中等

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait
#  after the ith day to get a warmer temperature. If there is no future day for
#  which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = []
#         value = 0
#         for i in range(len(temperatures)):
#             for j in range(i + 1, len(temperatures)):
#                 value += 1
#                 if temperatures[j] > temperatures[i]:
#                     break
#                 if j == len(temperatures) - 1 and temperatures[j] <= temperatures[i]:
#                     value = 0
#             answer.append(value)
#             value = 0
#         return answer

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans





        