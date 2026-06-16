# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#TC: O(n)
#SC: O(n)
class Solution:
    def swapPairs(self, head):

        tmp = head
        elements = []
        while tmp:
            elements.append(tmp.val)
            tmp = tmp.next
        
        for i in range(0, len(elements) - 1, 2):
            if i == len(elements) - 1:
                break
            tmp1 = elements[i + 1]
            elements[i + 1] = elements[i]
            elements[i] = tmp1


        ans = ListNode(5)
        tmp2 = ans
        for i in elements:
            tmp2.next = ListNode(i)
            tmp2 = tmp2.next

        head = ans.next
        return head

#recursive version
#TC: O(n)
#SC: O(n)
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        node1 = head
        node2 = head.next
        node3 = node2.next

        node1.next = self.swapPairs(node3)
        node2.next = node1

        return node2



#iterative version
#TC: O(n)
#SC: O(1)
class Solution:
    def swapPairs(self, head):
        node0 = dummy = ListNode(next = head)
        node1 = head
        while node1 and node1.next:
            node2 = node1.next
            node3 = node2.next

            node0.next = node2
            node2.next = node1
            node1.next = node3

            node0 = node1
            node1 = node3
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

x = Solution()
result = x.swapPairs(head)
while result:
    print(result.val)
    result = result.next