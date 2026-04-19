#

from typing import List
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        ans, cur = 0, 0
        tmp = {}
        for i,v in enumerate(nums):
            if v in tmp:
                tmp[v] += 1
            else:
                tmp[v] = 1
            
            left = i - k + 1
            if left < 0:
                continue

            for item in tmp:
                cur += pow(item, tmp[item])
            ans = max(ans, (cur % (pow(10,9) + 7)))
            cur = 0

            if tmp[nums[left]] > 1:
                tmp[nums[left]] -= 1
            else:
                del tmp[nums[left]]
        return ans
            
            

        