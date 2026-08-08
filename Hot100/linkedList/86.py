# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import *

#time complexity: O(n)
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        
        left = []
        right = []

        cur = head
        while cur:
            if cur.val < x:
                left.append(cur.val)
            else:
                right.append(cur.val)
            cur = cur.next
        
        dummy = ListNode()
        cur = dummy
        for i in left + right:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next