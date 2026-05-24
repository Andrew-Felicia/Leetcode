# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        elements = []
        tmp = head
        while tmp:
            elements.append(tmp.val)
            tmp = tmp.next

        m = len(elements) // k
        for i in range(m):
            elements[i * k : i * k + k] = elements[i * k : i * k + k][::-1]
        
        ans = ListNode(5)
        tmp1 = ans
        for i in elements:
            tmp1.next = ListNode(i)
            tmp1 = tmp1.next
        return ans.next