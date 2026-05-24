from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        n = len(height)
        left = [height[0]] + [0] * (n - 1)
        right = [0] * (n - 1) + [height[n - 1]]

        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        
        for i in range(n):
            result += min(left[i], right[i]) - height[i]
        return result