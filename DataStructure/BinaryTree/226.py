# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        self.invertTree_helper(root)
        return root

    def invertTree_helper(self, root):
        if not root:
            return
        if root and not root.left and not root.right:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree_helper(root.left)
        self.invertTree_helper(root.right)
        