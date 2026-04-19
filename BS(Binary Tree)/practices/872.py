# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, root):
        result = []
        if not root:
            return []
        if root.left == None and root.right == None:
            result.append(root.val)
        result.extend(self.dfs(root.left))
        result.extend(self.dfs(root.right))
        return result
    
#altenative solution
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.dfs(root.left) + self.dfs(root.right)