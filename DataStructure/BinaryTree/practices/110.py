# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        if root and not root.left and not root.right:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        

    #return the height of a tree
    def height(self, root):
        if not root:
            return 0
        elif root and not root.left and not root.right:
            return 1
        else:
            return 1 + max(self.height(root.left), self.height(root.right))