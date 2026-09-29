def canConstruct(ransomNote: str, magazine: str) -> bool:
        magazine_set = {}
        for i in magazine:
            if i in magazine_set:
                magazine_set[i] += 1
            else:
                magazine_set[i] = 1


        for i in ransomNote:
            if i not in magazine_set:
                return False
            if magazine_set[i] <= 0:
                return False
            magazine_set[i] -= 1
        return True


ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))