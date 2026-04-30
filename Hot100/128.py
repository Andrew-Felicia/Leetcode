from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(nums)

        #remove duplicates from sorted_nums.
        sorted_nums_withoutDuplicates = []
        sorted_nums_withoutDuplicates.append(sorted_nums[0])
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i] == sorted_nums_withoutDuplicates[-1]:
                continue
            sorted_nums_withoutDuplicates.append(sorted_nums[i])

        #count the length of the longest consecutive elements sequence.
        tmp = sorted_nums_withoutDuplicates[0]
        counts = 1
        ans = 1
        for i in range(1, len(sorted_nums_withoutDuplicates)):
            if sorted_nums_withoutDuplicates[i] - tmp == 1:
                counts += 1
                ans = max(ans, counts)
            else:
                counts = 1
            tmp = sorted_nums_withoutDuplicates[i]
        return ans
    

class Solution:
    #O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) #removed duplicates
        ans = 0
        for x in nums_set:
            if x - 1 in nums_set:
                continue
            #x is the smallest elements in the consecutive sequence
            y = x + 1
            while y in nums_set:
                y += 1
            ans = max(ans, y - x)
        return ans