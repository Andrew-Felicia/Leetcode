
#return the subset list of the given list, with this format below:
    #[[1],[3],[1,3]]
def subset(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [nums]
    else:
        result = []
        first = nums[0:1]
        remaining = nums[1:]
        for i in subset(remaining):
            result.append(i)
            result.append(first + i)
        result += [first]
        return result
    
# s = [5,1,6]
# result = subset(s)
# print(result)

def calculateXor(nums):
    result = 0
    s = subset(nums)
    for i in s:
        tmp = i[0]
        for j in i[1:]:
            tmp ^= j
        result += tmp
    return result

s = [1,3]
result = calculateXor(s)
print(result)



class Solution:
    def subsetXORSum(self, nums) -> int:
        return self.calculateXor(nums)
    

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
    

    def calculateXor(self, nums):
        result = 0
        s = self.subset(nums)
        for i in s:
            tmp = i[0]
            for j in i[1:]:
                tmp ^= j
            result += tmp
        return result

#another solution
class Solution:
    def subsetXORSum(self, nums) -> int:
        res = 0
        n = len(nums)
        for num in nums:
            res |= num
        return res << (n - 1)