# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head and not head.next:
            return head

        buffer = set()
        cur = head
        prev = head
        buffer.add(cur.val)
        cur = cur.next

        while cur:
            if cur.val in buffer:
                prev.next = cur.next
            else:
                buffer.add(cur.val)
                prev = prev.next
            cur = cur.next
        return head

class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        buffer = set()
        while cur:
            if cur.val in buffer:
                prev.next = cur.next
            else:
                buffer.add(cur.val)
                prev = cur
            cur = cur.next
        return head