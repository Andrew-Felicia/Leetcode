# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
#         if head.next.next == None:
#             return [-1,-1]

#         s = 2
#         tmp = []
#         prev = head
#         head = head.next
#         next_ = head.next

#         while next_.next != None:
#             if head.val == prev.val or head.val == next_.val:
#                 prev = prev.next
#                 head = head.next
#                 next_ = next_.next
#                 s += 1
#             if head.val > prev.val and head.val > next_.val:
#                 tmp.append(s)
#                 prev = prev.next
#                 head = head.next
#                 next_ = next_.next
#                 s += 1
#             if head.val < prev.val and head.val < next_.val:
#                 tmp.append(s)
#                 prev = prev.next
#                 head = head.next
#                 next_ = next_.next
#                 s += 1
#         if head.val > prev.val and head.val > next_.val:
#             tmp.append(s)
#         if head.val < prev.val and head.val < next_.val:
#             tmp.append(s)

#         if len(tmp) == 1 or len(tmp) == 0:
#             return [-1,-1]
#         elif len(tmp) == 2:
#             return [tmp[1] - tmp[0],tmp[1] - tmp[0]]
#         else:
#             tmp1 = [tmp[i] - tmp[i - 1] for i in range(1,len(tmp))]
#             return [min(tmp1), max(tmp1)]




class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if head.next.next == None:
            return [-1, -1]

        s = 2
        tmp = []
        prev = head
        head = head.next
        next_ = head.next

        while next_:
            if (head.val > prev.val and head.val > next_.val) or \
               (head.val < prev.val and head.val < next_.val):
               tmp.append(s)
            prev = prev.next
            head = head.next
            next_ = next_.next
            s += 1
        
        if len(tmp) <= 1:
            return [-1, -1]
        else:
            maxDis = tmp[-1] - tmp[0]
            minDis = min(tmp[i] - tmp[i - 1] for i in range(1, len(tmp)))
            return [minDis, maxDis]
        
            


         

        