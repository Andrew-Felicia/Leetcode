from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helperRec(s, left, right):
            if len(s) == 2 * n:
                result.append(''.join(s))
                return
            if left < n:
                s.append("(")
                helperRec(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(")")
                helperRec(s, left, right + 1)
                s.pop()
        
        helperRec([], 0, 0)
        return result