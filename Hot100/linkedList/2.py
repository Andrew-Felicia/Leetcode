# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # digit sum
            s = v1 + v2 + carry
            carry = s // 10
            digit = s % 10

            curr.next = ListNode(digit)
            curr = curr.next

            # move forward
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next