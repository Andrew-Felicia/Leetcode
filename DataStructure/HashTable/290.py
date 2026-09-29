def wordPattern(pattern: str, s: str) -> bool:
        pattern_set = {}
        s_set = {}
        for i in pattern:
            if i in pattern_set:
                pattern_set[i] += 1
            else:
                pattern_set[i] = 1

        for j in s.split(" "):
            if j in s_set:
                s_set[j] += 1
            else:
                s_set[j] = 1
        
        sorted_pattern_set = dict(sorted(pattern_set.items(), key = lambda item : item[1]))
        sorted_s_set = dict(sorted(s_set.items(), key = lambda item : item[1]))

        s1 = list(sorted_pattern_set.values())
        s2 = list(sorted_s_set.values())
        return s1 == s2



pattern = "abba"
s = "dog cat cat dog"

print(wordPattern(pattern, s))