# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root) -> bool:
        tmp = self.dfs(root)
        return all(x == tmp[0] for x in tmp)

    def dfs(self, root):
        if not root:
            return []
        if root and not root.left and not root.right:
            return [root.val]
        return [root.val] + self.dfs(root.left) + self.dfs(root.right)
    
    
        