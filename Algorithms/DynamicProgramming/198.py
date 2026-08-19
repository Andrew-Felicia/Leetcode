# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         #return all possible money, in list
#         ans = []
#         def rec(i, cur):
#             if i <= len(nums) - 1:
#                 cur += nums[i]
#             if i == len(nums) - 1 or i == len(nums) - 2 or i >= len(nums):
#                 ans.append(cur)
#                 return
#             else:
#                 for step in range(2, len(nums)):
#                     return rec(i + step, cur)
#         rec(0,0)
#         rec(1,0)

#         return max(ans)


from typing import List
from functools import cache

#recursive function
class Solution:
    def rob(self, nums: List[int]) -> int:
        #represent how much you can rob from num[0] to num[i] at most, return a int number
        @cache
        def rec(i):
            if i < 0:
                return 0
            else:
                return max(rec(i - 1), rec(i - 2) + nums[i])
        return rec(len(nums) - 1)

#递推
# 直接翻译的话，dfs(i) 翻译成 f[i]。
# 但记忆化搜索会访问 dfs(−2) 和 dfs(−1)，f[−2] 和 f[−1] 下标越界了。
# 解决办法：在 f 数组的前面插入两个 0，把 f 数组整体往右偏移 2 位。偏移后，dfs(i) 翻译成 f[i+2]。
# 注意只有 f 发生了偏移，nums 并没有偏移。

class Solution:
    def rob(self, nums: List[int]) -> int:
        f = [0] * (len(nums) + 2)
        for i, x in enumerate(nums):
            f[i + 2] = max(f[i + 1], f[i] + x)
        return f[-1]

#对递推进行空间优化
class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)
        return f1

        