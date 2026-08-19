# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         result = TreeNode(target.val)
#         self.dfs(cloned, target.val, result)
#         return result.left

#     def dfs(self, root, value, result):
#         if not root:
#             return
#         if root.val == value:
#             result.left = root
#             return
#         self.dfs(root.left, value, result)
#         self.dfs(root.right, value, result)




# can handle with the tree with same value.        
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None or original is target:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or \
               self.getTargetCopy(original.right, cloned.right, target)


        