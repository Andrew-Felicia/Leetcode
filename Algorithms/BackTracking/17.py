class Solution:
    def letterCombinations(self, digits):
        words = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"],
        "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], 
         "8":["t","u","v"], "9":["w","x","y","z"]}

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return words[digits]
        else:
            result = []
            current = digits[0]
            remaining = digits[1:]
            for i in words[current]:
                for j in self.letterCombinations(remaining):
                    result.append(i + j)
            return result
            
