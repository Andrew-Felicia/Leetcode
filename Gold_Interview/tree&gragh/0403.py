# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *

class Solution:
    def listOfDepthRec(self, tree, level, res):
        if not tree:
            return
        if len(res) <= level:
            res.append([])

        res[level].append(tree.val)

        self.listOfDepthRec(tree.left, level + 1, res)
        self.listOfDepthRec(tree.right, level + 1, res)

    def listOfDepth(self, tree: Optional[TreeNode]) -> List[Optional[ListNode]]:
        res = []
        self.listOfDepthRec(tree, 0, res)

        ans = []
        for i in res:
            dummy = ListNode()
            head = dummy
            for j in i:
                head.next = ListNode(j)
                head = head.next
            ans.append(dummy.next)
        return ans