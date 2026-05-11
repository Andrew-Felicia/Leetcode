# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        tmp = head
        elements = []
        while tmp:
            elements.append(tmp.val)
            tmp = tmp.next

        elements.sort()

        ans = ListNode(5)
        tmp1 = ans
        for i in elements:
            tmp1.next = ListNode(i)
            tmp1 = tmp1.next
        return ans.next
