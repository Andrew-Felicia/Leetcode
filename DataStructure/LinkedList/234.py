# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#this function will print this linked list from right to left.
# def f(node):
#     if node is None:
#         return
#     f(node.next)
#     print(node.val)  # note: if put this line above f(node.next),will print from left to right.

# f(head)

#TC: O(n)
#SC: O(n)
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         elements = []
#         while head.next:
#             elements.append(head.val)
#             head = head.next
#         elements.append(head.val)

#         for i in range(len(elements)):
#             j = len(elements) - i - 1
#             if elements[i] != elements[j]:
#                 return False
#             if i > j:
#                 break
#         return True


class Solution:
    def findMiddle(self, head):
        """
        using slow and fast pointer to find the middle node of the linkedlist.
        for example:
        1.even number nodes.
        1 -> 2 -> 3 -> 4
                  ^
                  |
                  slow(mid is here)
        2.odd number nodes.
        1 -> 2 -> 3
             ^
             |
             slow(mid is here)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseLinkedList(self, head):
        prev, cur = None, head
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def isPalindrome(self, head) -> bool:
        """
        1.odd nodes
        original list:
        1 -> 2 -> 3 -> 2 -> 1

        after findmiddle and reverse
                null
                  ^
                  |
        1 -> 2 -> 3 <- 2 <- 1
        ^                   ^
        |                   |
        head               head2
    
        2.even nodes
        original list
        1 -> 2 -> 3 -> 3 -> 2 -> 1

        after findmiddle and reverse:
                     null
                       ^
                       |
        1 -> 2 -> 3 -> 3 <- 2 <- 1
        ^                        ^
        |                        |
        head                    head2

        """
        mid = self.findMiddle(head)
        head2 = self.reverseLinkedList(mid)

        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True