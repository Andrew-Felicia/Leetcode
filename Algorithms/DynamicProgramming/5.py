# 5. Longest Palindromic Substring
# 已解答
# 中等

# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

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


        