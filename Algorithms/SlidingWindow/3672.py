#

from typing import List
class Solution:
    def modeWeight(self, nums: List[int], k: int) -> int:
        ans = 0
        tmp = {}
        for i,v in enumerate(nums):
            if v in tmp:
                tmp[v] += 1
            else:
                tmp[v] = 1


            left = i - k + 1
            if left < 0:
                continue

            mode = max(tmp.items(), key=lambda item: (item[1], -item[0]))[0]
            ans += mode * tmp[mode]

            if tmp[nums[left]] > 1:
                tmp[nums[left]] -= 1
            else:
                del tmp[nums[left]]
        return ans



        