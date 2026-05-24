
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         #creating interweaving
#         cur = head
#         while cur:
#             cur.next = Node(cur.val, cur.next)
#             cur = cur.next.next

#         #copy the random pointers
#         cur = head
#         while cur:
#             cur.next.random = cur.random
#             cur = cur.next.next

#         #return the result
#         cur = dummy = Node(5, head)
#         while cur:
#             cur.next = cur.next.next
#             cur = cur.next

#         return dummy.next


class Solution:
    def copyRandomList(self, head):
        #creating interweaving
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        #copy the random pointers
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        #return the result
        cur = dummy = Node(5, head)
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next

        return dummy.next