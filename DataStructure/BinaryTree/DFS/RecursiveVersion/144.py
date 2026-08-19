# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        def preorder(root):
            if root == None:
                return
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)

        result = []
        preorder(root)
        return result

# TC:O(n)