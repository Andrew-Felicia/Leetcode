from collections import Counter
from typing import List

def majorityElement(nums: List[int]) -> int:
    nums_dict = Counter(nums)
    nums_dict_sorted = dict(sorted(nums_dict.items(), key = lambda item:item[1], reverse = True))
    first = next(iter(nums_dict_sorted))
    return first

nums = [6,5,5]
print(majorityElement(nums))