# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:

        self.maxSum = float('-inf')
        
        #return the max path sum of the tree. the path is left branch + root or right branch + root.
        def maxSum(node):
            if not node:
                return 0
            
            left = max(0, maxSum(node.left))
            right = max(0, maxSum(node.right))
            
            #record and update the maximum path(from left to root to right) sum
            self.maxSum = max(self.maxSum, node.val + left + right )

            return node.val + max(left, right)

        maxSum(root)
        return self.maxSum
