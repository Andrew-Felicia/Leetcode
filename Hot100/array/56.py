from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        merged = []

        for interval in intervals:
            #did not overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


# def parse_intervals(s: str):
#     s = s.strip()
#     s = s.replace("[[", "").replace("]]", "")
#     if not s:
#         return []

#     parts = s.split("],[")

#     intervals = []
#     for p in parts:
#         a, b = p.split(",")
#         intervals.append([int(a), int(b)])
#     return intervals


# def merge(intervals):
#     intervals.sort(key=lambda x: x[0])
#     merged = []

#     for interval in intervals:
#         if not merged or merged[-1][1] < interval[0]:
#             merged.append(interval)
#         else:
#             merged[-1][1] = max(merged[-1][1], interval[1])
#     return merged


# # ========== MAIN (ACM style) ==========
# s = input().strip()           # 读取类似 "[[1,3],[2,6],[8,10]]"
# intervals = parse_intervals(s)
# ans = merge(intervals)

# print(ans)