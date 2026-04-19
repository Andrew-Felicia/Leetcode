# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        return self.dfs(root)

    #Your current code has a logic bug common in tree problems: if a node has 
    #only one child, min(self.dfs(root.left), self.dfs(root.right)) will pick 
    #the empty side (which returns 0) and incorrectly identify that node as having a depth of 1.
    
    # def dfs(self, root):
    #     if not root:
    #         return 0
    #     if root and not root.left and not root.right:
    #         return 1
    #     return 1 + min(self.dfs(root.left), self.dfs(root.right))

    def dfs(self, root):
        if not root:
            return 0
        if not root.left:
            return 1 + self.dfs(root.right)
        if not root.right:
            return 1+ self.dfs(root.left)
        return 1 + min(self.dfs(root.left), self.dfs(root.right))

    
        