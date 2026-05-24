#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        start, end = 0, 0  # indices of best palindrome
        
        for i in range(len(s)):
            # odd length palindromes
            len1 = self.expand(s, i, i)
            # even length palindromes
            len2 = self.expand(s, i, i + 1)
            
            max_len = max(len1, len2)
            if max_len > end - start + 1:
                # compute new boundaries
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        # when loop stops, left/right are one step beyond the palindrome
        return right - left - 1   # palindrome length

        
# @lc code=end



# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 0:
#             return ""
#         elif len(s) == 1:
#             return s
#         else:
#             tmp = [] #record every palindrome we found so far
#             n = len(s)
#             for i in range(n):
#                 tmp.append(s[i])
#                 for j in range(i + 1, n):
#                     if self.is_Palindrome(s[i:j + 1]):
#                         tmp.append(s[i:j + 1])

#             #find the longest palindrome
#             result = tmp[0]
#             for i in tmp:
#                 if len(i) > len(result):
#                     result = i

#             return result

#     def is_Palindrome(self, s):
#         s1 = s[::-1]
#         if s1 == s:
#             return True
#         else:
#             return False



# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) <= 1:
#             return s
        
#         start, end = 0, 0  # indices of best palindrome
        
#         for i in range(len(s)):
#             # odd length palindromes
#             len1 = self.expand(s, i, i)
#             # even length palindromes
#             len2 = self.expand(s, i, i + 1)
            
#             max_len = max(len1, len2)
#             if max_len > end - start + 1:
#                 # compute new boundaries
#                 start = i - (max_len - 1) // 2
#                 end = i + max_len // 2
        
#         return s[start:end + 1]
    
#     def expand(self, s, left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
            
#         # when loop stops, left/right are one step beyond the palindrome
#         return right - left - 1   # palindrome length


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_left = ans_right = 0

        # 奇回文串
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # 循环结束后，s[l+1] 到 s[r-1] 是回文串
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开区间

        # 偶回文串
        for i in range(n - 1):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开区间

        return s[ans_left: ans_right]