# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeNodes(self, head):
        M = head.next
        T = M.next
        head = head.next

        while T:
            if T.val != 0 and T != M:
                M.val += T.val
            if T.val == 0:
                M.next = T.next
                M = M.next
            T = T.next

        return head