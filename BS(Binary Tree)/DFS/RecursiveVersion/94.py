# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
#            1
#           / \
#          2   5
#         / \
#        3   4
#
# [3,2,4,1,5]
class Solution:
    def inorderTraversal(self, root):
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
            

        result = []
        inorder(root)
        return result

#TC: O(N)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

sol = Solution()
result = sol.inorderTraversal(root)
print(result)