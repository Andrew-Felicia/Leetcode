# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        return self.binaryTreePathsHelper(root)
        


    #return all root-to-leaf paths in any order, with this format below:
    #["1->2->5","1->3"]
    def binaryTreePathsHelper(self, root):
        if not root:
            return []
        elif root and not root.left and not root.right:
            return [f"{root.val}"]
        else:
            result = []
            for i in self.binaryTreePathsHelper(root.left):
                result.append(f"{root.val}" + "->" + i)
            for i in self.binaryTreePathsHelper(root.right):
                result.append(f"{root.val}" + "->" + i)
            return result
            