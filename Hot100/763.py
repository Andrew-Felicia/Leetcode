from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_char = {char : index for index, char in enumerate(s)}

        start = 0
        end = 0
        ans = []
        for i, v in enumerate(s):
            end = max(end, last_char[v])
            if i == end:
                ans.append(i - start + 1)
                start = i + 1

        return ans