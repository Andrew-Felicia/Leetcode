from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[i] denotes if s[:i] can be segmented into a space-separated 
        #sequence of one or more dictionary words.
        dp = [False] * (len(s) + 1)
        dp[0] = True 
        wordDict = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in  wordDict:
                    dp[i] = True
        return dp[len(s)]