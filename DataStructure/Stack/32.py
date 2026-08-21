#time limit exceed
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if self.wellFormedParentheses(s[i:j + 1]):
                    ans = max(ans, len(s[i: j + 1]))
        return ans


    #return if s is a well formed parentheses sequences.
    def wellFormedParentheses(self, s):
        result = []
        for i in s:
            if i == "(":
                result.append(i)
            elif i == ")" and result:
                result.pop()
            elif i == ")" and not result:
                 return False
        return len(result) == 0


