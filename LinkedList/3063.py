# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def frequenciesOfElements(self, head):
        tmp = {}
        result = ListNode()
        tmp1 = result
        while head:
            if head.val in tmp:
                tmp[head.val] += 1
            else:
                tmp[head.val] = 1
            head = head.next
        for value in tmp.values():
            tmp1.next = ListNode(value)
            tmp1 = tmp1.next
        return result.next
            
#one thing you should know is that, None is just None,None doesn't has any features.