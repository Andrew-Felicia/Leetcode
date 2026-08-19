from typing import List
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans,left = 0, 0
        cur = defaultdict(int)
        
        for right, v in enumerate(s):
            cur[v] += 1

            while cur[v] > 2:
                cur[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans