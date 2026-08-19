# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         n = len(nums)
#         for i in range(n - k + 1):
#             result.append(max(nums[i:i + k]))
#         return result
        
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()       # will store indices, values decrease inside deque
        res = []
        
        for i, x in enumerate(nums):
            
            # 1. Remove smaller elements from the right
            while q and nums[q[-1]] <= x:
                q.pop()
            
            # Push current index
            q.append(i)
            
            # 2. Remove the left element if it’s outside window
            if q[0] <= i - k:
                q.popleft()
            
            # 3. Append result when window first becomes size k
            if i >= k - 1:
                res.append(nums[q[0]])   # biggest element in window is q[0]
        
        return res

