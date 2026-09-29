# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def sortedArrayToBSTRec(self, nums, left, right):
        if left > right:
            return
        #choose the upper right middle one.
        mid = left + (right - left + 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTRec(nums, left, mid - 1)
        root.right = self.sortedArrayToBSTRec(nums, mid + 1, right)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBSTRec(nums, 0, len(nums) - 1)