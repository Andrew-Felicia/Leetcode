# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Your code only checks the direct children of each node.
# But BST requires:
# ALL nodes in left subtree < root
# ALL nodes in right subtree > root
# not just immediate children.
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         elif not root.left and not root.right:
#             return True
#         elif root.left and not root.right:
#             if root.left.val >= root.val:
#                 return False
#             return self.isValidBST(root.left)
#         elif not root.left and root.right:
#             if root.right.val <= root.val:
#                 return False
#             return self.isValidBST(root.right)
#         else:
#             if root.left.val >= root.val:
#                 return False
#             if root.right.val <= root.val:
#                 return False
#             return self.isValidBST(root.left) and self.isValidBST(root.right)




class Solution:
    def isValidBST(self, root) -> bool:
        def helper(root, low, high):
            if not root:
                return True
            elif root.val <= low or root.val >= high:
                return False
            else:
                return helper(root.left, low, root.val) and \
                helper(root.right, root.val, high)

        return helper(root, float('-inf'), float('inf'))