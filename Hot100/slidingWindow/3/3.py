#

from typing import List
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        cnt = defaultdict(int)  # 维护从下标 left 到下标 right 的字符及其出现次数
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:  # 窗口内有重复字母
                cnt[s[left]] -= 1  # 移除窗口左端点字母
                left += 1  # 缩小窗口
            ans = max(ans, right - left + 1)  # 更新窗口长度最大值
        return ans