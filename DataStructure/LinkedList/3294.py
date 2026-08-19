"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node):
        result = []
        l = r = node
        while l:
            result.insert(0, l.val)
            l = l.prev
        r = r.next
        while r:
            result.append(r.val)
            r = r.next
        return result