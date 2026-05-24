#Caterpillar Crawling

#Memory limit exceeded
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         #count which and how many letters exist in t
#         t_dict = {}
#         for i in t:
#             if i in t_dict:
#                 t_dict[i] += 1
#             else:
#                 t_dict[i] = 1

#         ans = []
#         window_dict = {}
#         m, n = len(s), len(t)
#         j = 0
#         for i in range(m):
#             if s[i] in window_dict:
#                 window_dict[s[i]] += 1
#             else:
#                 window_dict[s[i]] = 1
#             #shrink
#             while self.ifWindowContainsT(t_dict, window_dict):
#                 ans.append(s[j:i + 1])
#                 if window_dict[s[j]] > 1:
#                     window_dict[s[j]] -= 1
#                 else:
#                     del window_dict[s[j]]
#                 j += 1
#         if not ans:
#             return ""
#         else:
#             minWindow = ans[0]
#             for i in ans:
#                 if len(i) < len(minWindow):
#                     minWindow = i
#             return minWindow
                
    
#     #python doesn't have this:if !(key in window_dict and t_dict[key] <= window_dict[key]):
#     #but it have this: !=
#     #decide if window_dict contains all of the letters in t_dict, including duplicates.
#     def ifWindowContainsT(self, t_dict, window_dict):
#         for key in t_dict:
#             if not (key in window_dict and t_dict[key] <= window_dict[key]):
#                 return False
#         return True

from collections import Counter
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        need = len(t_count)

        #Track the window details: (Window_length, left_index, right_index)
        window_count = {}
        
        have = 0

        res = (float('inf'), None, None)
        
        #Caterpillar Crawling
        left = 0
        #moving forward
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and t_count[char] == window_count[char]:
                have += 1
            #shrinking
            while have == need:
                #updating
                current_window_len = right - left + 1
                if current_window_len < res[0]:
                    res = (current_window_len, left, right)

                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1

                left += 1
        return s[res[1]: res[2] + 1] if res[0] != float('inf') else ""


