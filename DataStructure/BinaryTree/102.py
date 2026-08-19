# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]]
        else:
            left = self.levelOrder(root.left)
            right = self.levelOrder(root.right)

            result = []
            for i in range(max(len(left), len(right))):
                a = left[i] if i < len(left) else []
                b = right[i] if i < len(right) else []
                result.append(a + b)

            return [[root.val]] + result