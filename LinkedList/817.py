# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head, nums) -> int:
        nums_set = set(nums)
        result = 0
        while head:
            if head.val in nums_set and(not head.next or head.next.val not in nums_set):
                result += 1
            head = head.next
        return result