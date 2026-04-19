# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
class Solution:
    def isSymmetric(self, root) -> bool:
        return self.mirrorTree(root.left, root.right)

    def mirrorTree(self, root1, root2):
        if not root1 or not root2:
            return root1 == root2
        return root1.val == root2.val and self.mirrorTree(root1.left, root2.right) \
        and self.mirrorTree(root1.right, root2.left)