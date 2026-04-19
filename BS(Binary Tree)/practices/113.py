# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum: int):
        result = []
        tmp = self.permutations(root)
        for i in tmp:
            if i and sum(i) == targetSum:
                result.append(i)
        return result

    #return all the possible situations of root-to-leaf list
    #with this format:[[5,4,11,2],[5,8,4,5]]
    def permutations(self, root):
        if not root:
            return []
        elif root and not root.left and not root.right:
            return [[root.val]]
        else:
            result = []
            for i in self.permutations(root.left):
                if i:
                    result.append([root.val] + i)
            for i in self.permutations(root.right):
                if i:
                    result.append([root.val] + i)
            return result
            

root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

sol  = Solution()
result = sol.permutations(root)
print(result)
        
        