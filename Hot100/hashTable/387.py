# Time:  O(n)
# Space: O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        for i, c in enumerate(s):
            if frequency[c] == 1:
                return i
        return -1