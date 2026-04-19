# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#

#just keep in mind that even if we have this:root.val == min(root.left.val, root.right.val)
#  for each internal node of the tree, max(root.left.val, root.right.val) may not be the second
#minimum element inside this tree.
#for example:
#       1
#      / \
#     1   3
#    / \
#   1   2


class Solution:
    def findSecondMinimumValue(self, root) -> int:
        tmp = self.dfs(root)
        if all(x == tmp[0] for x in tmp):
            return -1
        minVal = min(tmp)

        for _ in range(tmp.count(minVal)):
            tmp.remove(minVal)
        return min(tmp)

        
    def dfs(self, root):
        if not root:
            return []
        if root and not root.left and not root.right:
            return [root.val]
        return [root.val] + self.dfs(root.left) + self.dfs(root.right)
        
        