# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        return self.dfs(root)

    # def dfs(self, root):
    #     if not root:
    #         return 0
    #     if root and not root.left and not root.right:
    #         return 0
    #     if root.left and not root.left.left and not root.left.right:
    #         return root.left.val + self.dfs(root.right)
    #     return self.dfs(root.left) + self.dfs(root.right)
    
    
    def dfs(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.dfs(root.right)
        return self.dfs(root.left) + self.dfs(root.right)