# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#recursive version
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or head.next == None:
#             return head
#         else:
#             first = head.val
#             reversedList = self.reverseList(head.next)

#             tail = head
#             while tail.next:
#                 tail = tail.next
#             tail.next = ListNode(first)
#             return reversedList

#iterative version
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        elements = elements[::-1]

        ans = ListNode(5)
        tmp = ans
        for i in elements:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return ans.next