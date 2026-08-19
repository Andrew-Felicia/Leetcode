
#for loop recursive solution.
class Solution:
    def subsets(self, nums):
        if len(nums) == 1:
            return [[], nums]
        else:
            first = nums[0:1]
            result = self.subsets(nums[1:])
            for i in self.subsets(nums[1:]):
                result.append(first + i)
            return result
        


#backTracking 

class Solution1:
    def subsets(self, nums):
        n = len(nums)
        ans = []
        path = []

        #将从位置i开始到达叶子的path加入到ans中
        def dfs(i: int) -> None:
            if i == n:  
                ans.append(path.copy())  # 复制 path，也可以写 path[:].Each .copy() creates a new list object.
                return                   #path is one single list object reused during backtracking.
                                         # ans.append(path) → store a reference to the same list
                                         # ans.append(path.copy()) → store a snapshot of the list at that moment
                                         # Without .copy(), all subsets in ans will end up the same.
                                         # Key rule (memorize this)
                                        # Whenever a mutable object is reused and later modified,
                                        # store a copy, not the reference.
                                        # When is ans.append(path) OK?
                                        # Only if:
                                        # path will never be modified again

            # 不选 nums[i]
            dfs(i + 1) 

            # 选 nums[i]
            path.append(nums[i])
            dfs(i + 1)  # 考虑下一个数 nums[i+1] 选或不选
            path.pop()  # 恢复现场，撤销 path.append(nums[i])

        dfs(0)
        return ans
#结合二叉树来想， dfs()就是一个选或者不选的混合， 选择往下走的那个递归返回之后不能影响其他递归，所以要
#撤销操作.
#Why path.pop() is required
# After finishing “choose nums[i]”, we must remove it, because:
# path is shared by all recursive calls
# Python passes lists by reference
# If you don’t pop(), the element stays and pollutes other branches

Sol = Solution1()
print(Sol.subsets([1,2,3]))



#Bitmask
class Solution:
    def subsets(self, nums):
        n = len(nums)
        ans = []

        for mask in range(1 << n):  # from 0 to 2^n - 1
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            ans.append(subset)

        return ans

#iterative
class Solution:
    def subsets(self, nums):
        ans = [[]]   # start with empty subset

        for num in nums:
            new_subsets = []
            for subset in ans:
                new_subsets.append(subset + [num])
            ans.extend(new_subsets)

        return ans
