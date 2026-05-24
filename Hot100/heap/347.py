from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        sorted_nums_dict = dict(sorted(nums_dict.items(), key = lambda item : item[1], reverse = True))
        
        result = []
        for i in sorted_nums_dict:
            result.append(i)
        return result[:k]