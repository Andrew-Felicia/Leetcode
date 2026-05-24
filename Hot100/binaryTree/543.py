# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#The main issue with your current logic is a classic "Binary Tree Diameter" pitfall: The longest path does not necessarily pass through the root.
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root.left and not root.right:
#             return 0
#         elif not root.left and root.right:
#             return 1 + self.deepest(root.right)
#         elif root.left and not root.right:
#             return 1 + self.deepest(root.left)
#         else:
#             return 2 + self.deepest(root.left) + self.deepest(root.right)

#     #return the most deep length in the tree
#     def deepest(self, root):
#         if not root.left and not root.right:
#             return 0
#         elif not root.left and root.right:
#             return 1 + self.deepest(root.right)
#         elif root.left and not root.right:
#             return 1 + self.deepest(root.left)
#         else:
#             return max(self.deepest(root.left), self.deepest(root.right)) + 1



#tree depth:
#   1      -> 1
#################
#   1
#  / \
# 3   3    -> 2
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.Diameter = 0
        
        #return the height of a BST tree
        def deepestHeight(node):
            if not node:
                return 0

            left = deepestHeight(node.left)
            right = deepestHeight(node.right)
            
            #the diameter at this node is it's left subtree height plus it's right subtree height.
            #record/update the maximum diamter.
            self.Diameter = max(self.Diameter, left + right)

            ## Return the height of this node to its parent
            return 1 + max(left, right)
        
        deepestHeight(root)
        return self.Diameter