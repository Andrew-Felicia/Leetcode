
def minWindow(s: str, t: str) -> str:
    #count which and how many letters exist in t
    t_dict = {}
    for i in t:
        if i in t_dict:
            t_dict[i] += 1
        else:
            t_dict[i] = 1

    ans = float('inf')
    window_dict = {}
    m, n = len(s), len(t)
    j = 0
    for i in range(m):
        if s[i] in window_dict:
            window_dict[s[i]] += 1
        else:
            window_dict[s[i]] = 1

        while ifWindowContainsT(t_dict, window_dict):
            ans = min(ans, len(window_dict))
            if window_dict[s[j]] > 1:
                window_dict[s[j]] -= 1
            else:
                del window_dict[s[j]]
            j += 1
        return ans
            

#python doesn't have this:if !(key in window_dict and t_dict[key] <= window_dict[key]):
#but it have this: !=
#decide if window_dict contains all of the letters in t_dict, including duplicates.
def ifWindowContainsT(t_dict, window_dict):
    for key in t_dict:
        if not (key in window_dict and t_dict[key] <= window_dict[key]):
            return False
    return True