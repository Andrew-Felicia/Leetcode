from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        head = 0
        while slow != head:
            slow = nums[slow]
            head = nums[head]

        return slow
        