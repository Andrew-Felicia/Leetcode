#solution 1
class Solution:
    def checkEqualPartitions(self, nums, target) -> bool:
        subset = self.subset(nums)
        tmp = []

        #filter the subset whose product is target, and store in tmp
        for i in subset:
            if self.product(i) == target:
                tmp.append(i)
        

        index = {value: i for i, value in enumerate(nums)}
        n = len(nums)
        full_mask = (1 << n) - 1   # 11111

        def to_mask(subset):
            mask = 0
            for x in subset:
                mask |= 1 << index[x]
            return mask

        for i in range(len(tmp)):
            for j in range(i + 1, len(tmp)):
                m1 = to_mask(tmp[i])
                m2 = to_mask(tmp[j])
                if (m1 & m2) == 0 and (m1 | m2) == full_mask:
                    return True
        return False

    #return the subset list of the given list, with this format below:
    #[[1],[3],[1,3]]
    def subset(self, nums):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            result = []
            first = nums[0:1]
            remaining = nums[1:]
            for i in self.subset(remaining):
                result.append(i)
                result.append(first + i)
            result += [first]
            return result

    # return the product of every elements in list nums
    # [1,2,3] -> 6    [1] -> 1   
    def product(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            tmp = nums[0]
            for i in nums[1:]:
                tmp *= i
            return tmp
        


#solution 2

class Solution:
    def checkEqualPartitions(self, nums, target):
        def checkEqualPartitionsRec(i, mul1, mul2):
            if i == len(nums):
                return mul1 == mul2 == target
            return checkEqualPartitionsRec(i + 1, mul1 * nums[i], mul2) or \
                   checkEqualPartitionsRec(i + 1, mul1, mul2 * nums[i])

        return checkEqualPartitionsRec(0, 1, 1)