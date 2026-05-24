# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        elements = self.kthSmallestHelper(root)
        elements.sort()
        return elements[k - 1]
        
    #return the all the values of the node in BST in list.
    def kthSmallestHelper(self, root):
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]
        else:
            return [root.val] + self.kthSmallestHelper(root.left) \
            + self.kthSmallestHelper(root.right)