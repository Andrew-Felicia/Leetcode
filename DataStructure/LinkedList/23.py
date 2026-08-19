# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        result = []
        for i in lists:
            result += self.extractList(i)

        result.sort()
        
        ans = ListNode(5) #dummy node
        tmp = ans
        for i in result:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return ans.next
            



    def extractList(self, listNode):
        tmp = listNode
        elements = []
        while tmp:
            elements.append(tmp.val)
            tmp = tmp.next
        return elements