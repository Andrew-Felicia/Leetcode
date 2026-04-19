class Solution:
    def letterCasePermutation(self, s):
        if not s:
            return []
        elif len(s) == 1 and s.isdigit():
            return [s]
        elif len(s) == 1 and s.isalpha():
            return [s.lower(), s.upper()]
        else:
            first = s[0]
            remaining = s[1:]
            result = []
            if first.isdigit():
                for i in self.letterCasePermutation(remaining):
                    result.append(first + i)
                return result
            else:
                for i in self.letterCasePermutation(remaining):
                    result.append(first.lower() + i)
                    result.append(first.upper() + i)
                return result
