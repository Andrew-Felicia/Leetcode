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

# data = {'apple': 5, 'banana': 2, 'cherry': 7}

# # Sort by value in ascending order
# sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

# print(sorted_data)
# # Output: {'banana': 2, 'apple': 5, 'cherry': 7}


# data = {'apple': 5, 'banana': 2, 'cherry': 7}

# # Sort by value in descending order
# sorted_data_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

# print(sorted_data_desc)
# # Output: {'cherry': 7, 'apple': 5, 'banana': 2}


# prices = {"apple": 1.5, "banana": 0.75, "orange": 1.25}

# # Get all values
# all_prices = prices.values()
# print(all_prices)  # Output: dict_values([1.5, 0.75, 1.25])

# # Convert to a standard list to look up by index
# prices_list = list(prices.values())
# print(prices_list[0])  # Output: 1.5





class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        character_set = {}
        word_set = {}
        for c, w in zip(pattern, s):
            if (c in character_set and character_set[c] != w) or (w in word_set and word_set[w] != c):
                return False
            character_set[c] = w
            word_set[w] = c
        return True