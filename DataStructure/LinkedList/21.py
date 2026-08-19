# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         result = ListNode(0)
#         tmp = result

#         while list1 != None and list2 != None:
#             if list1.val <= list2.val:
#                 tmp.next = ListNode(list1.val)
#                 tmp = tmp.next
#                 list1 = list1.next
#             else:
#                 tmp.next = ListNode(list2.val)
#                 tmp = tmp.next
#                 list2 = list2.next

#         if list1 == None:
#             while list2 != None:
#                 tmp.next = ListNode(list2.val)
#                 tmp = tmp.next
#                 list2 = list2.next
#         if list2 == None:
#             while list1 != None:
#                 tmp.next = ListNode(list1.val)
#                 tmp = tmp.next
#                 list1 = list1.next
#         return result.next
#
#code is right, but if you creat new node every time,leetcode will not let you pass the test



class Solution:
    def mergeTwoLists(self, list1, list2):
        result = ListNode(0)
        tmp = result

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next
        # Attach remaining nodes. Method2
        tmp.next = list1 if list1 else list2

        return result.next