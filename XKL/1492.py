from typing import List

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []
        for i in range(1, n + 1):
            if n % i == 0:
                factor.append(i)
        return -1 if k > len(factor) else factor[k - 1]