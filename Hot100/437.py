# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val

            count = prefix_sum[current_sum - targetSum]

            prefix_sum[current_sum] += 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            prefix_sum[current_sum] -= 1
            return count
            

        return dfs(root, 0)