# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Given the root of a binary tree, return its maximum depth.
class Solution:
    def maxDepth(self, root) -> int:
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0
        if root and not root.left and not root.right:
            return 1
        return 1 + max(self.dfs(root.left), self.dfs(root.right))