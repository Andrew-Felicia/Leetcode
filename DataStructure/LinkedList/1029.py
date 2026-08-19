# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        s = ""
        while head.next != None:
            s += str(head.val)
            head = head.next
        s += str(head.val)
        return int(s, 2)
        