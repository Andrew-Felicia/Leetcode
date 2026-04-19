#
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans, cur = 0, 0
        for i, v in enumerate(s):
            #right end enter the window
            if v in "aeiou":
                cur += 1

            left = i - k + 1  #left end of the window
            if left < 0:
                continue

            if cur > ans:     #update the answer
                ans = cur
            if ans == k:
                break
            
            #left end left the window
            if s[left] in "aeiou":
                cur -= 1

        return ans