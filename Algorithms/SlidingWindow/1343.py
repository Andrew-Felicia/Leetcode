#
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans, cur = 0, 0
        for i, v in enumerate(arr):
            cur += v

            left = i - k + 1
            if left < 0:
                continue

            if cur / k >= threshold:
                ans += 1
            
            cur -= arr[left]
        return ans

        