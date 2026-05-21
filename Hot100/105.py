# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        #construct O(1) searching map.
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        
        self.pre_root_idx = 0

        def arrayToTree(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_root_idx]
            root = TreeNode(root_val)
            self.pre_root_idx += 1

            root.left = arrayToTree(left, inorder_map[root_val] - 1)
            root.right = arrayToTree(inorder_map[root_val] + 1, right)
            return root

        return arrayToTree(0, len(inorder) - 1)