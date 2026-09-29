# class Solution:
#     def isUnique(self, astr: str) -> bool:
#         return len(set(astr)) == len(astr)


class Solution:
    def isUnique(self, astr: str) -> bool:
        if (len(astr) > 26) :
            return False
        mask = 0
        for char in astr:
            position = ord(char) - ord('a')
            bit = 1 << position
            if bit & mask:
                return False
            mask |= bit
        return True