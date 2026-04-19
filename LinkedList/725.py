# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head, k: int):
        result = []
        tmp = head

        #compute the size of this link list.And n store size.
        n = 0
        while tmp:
            n += 1
            tmp = tmp.next
        
        value = n // k
        remainder = n % k

        part_tail = head
        for i in range(k):
            part_head = part_tail
            part_size = value + (1 if i < remainder else 0)

            #cut and append the part
            while part_tail and part_size - 1:
                part_tail = part_tail.next
                part_size -= 1
            if part_tail:
                tmp1 = part_tail.next
            else:
                tmp1 = None
            if part_tail:
                part_tail.next = None
            result.append(part_head)

            part_head = tmp1
            part_tail = tmp1
        
        return result
                



        