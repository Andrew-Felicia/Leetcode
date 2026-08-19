from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(index, current_sum, remain_target):
            if index >= len(candidates) or remain_target < 0:
                return
            if remain_target == 0:
                result.append(list(current_sum))
                return

            current_sum.append(candidates[index])
            dfs(index, current_sum, remain_target - candidates[index])

            current_sum.pop()

            dfs(index + 1, current_sum, remain_target)

        
        dfs(0, [], target)
        return result