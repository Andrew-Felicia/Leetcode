# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """

        
#         #pre order traversal the tree, and return the node value in list
#         def preOrderTraversal(node):
#             if not node:
#                 return []
#             else:
#                 return [node.val] + preOrderTraversal(node.left) + preOrderTraversal(node.right)

#         elements = preOrderTraversal(root)

#         ans = TreeNode(5)
#         tmp = ans
#         for i in elements:
#             tmp.right = TreeNode(i)
#             tmp = tmp.right
#         return ans.right

from typing import List

class Solution:
    def flatten(self, root) -> None:
        if not root:
            return

        nodes = []
        def preOrderTraversal(node):
            if not node:
                return
            nodes.append(node)
            preOrderTraversal(node.left)
            preOrderTraversal(node.right)

        preOrderTraversal(root)

        tmp = root
        for i in range(len(nodes) - 1):
            tmp.left = None
            tmp.right = nodes[i + 1]
            tmp = tmp.right

        nodes[-1].left = None
        nodes[-1].right = None