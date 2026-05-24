from collections import defaultdict
class Solution:
    def singleNumber(self, nums) -> int:
        record = defaultdict(int)
        for i in nums:
            record[i] += 1
        for key in record:
            if record[key] == 1:
                return key