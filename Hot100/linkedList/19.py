# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#TC: O(n)
#SC: O(n)
class Solution:
    def removeNthFromEnd(self, head, n: int):
        elements = []
        while head:
            elements.append(head.val)
            head = head.next

        elements = elements[0:len(elements) - n] + elements[len(elements) - n + 1:]
        # elements = elements[::-1]
        # elements = elements[0:n - 1] + elements[n:]
        # elements = elements[::-1]

        ans = ListNode(5) #Dummy Node
        tmp = ans
        for i in elements:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return ans.next
    
#TC: O(n)
#SC: O(1)
class Solution:
    def removeNthFromEnd(self, head, n: int):
        #base case
        if not head.next and n == 1:
            return None

        #counts how many nodes.
        tmp = head
        counts = 0
        while tmp:
            tmp = tmp.next
            counts += 1
    
        #how many nodes before the node which needed to be removed.
        left = counts - n

        if left == 0: 
            return head.next
        

        tmp = head
        for i in range(0, left - 1):
            tmp = tmp.next
        tmp1 = tmp.next.next #the rest of the linked list.
        tmp.next = tmp1

        return head

      
        