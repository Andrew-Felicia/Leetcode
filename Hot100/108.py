# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            m = len(nums) // 2
            root = TreeNode(nums[m])
            root.left = self.sortedArrayToBST(nums[0:m])
            root.right = self.sortedArrayToBST(nums[m + 1:])
            return root
