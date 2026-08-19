from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
            
        result = []
        # Use deque for O(1) pops from the front
        queue = deque([root])
        
        while queue:
            # Number of nodes at the current level
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                # 1. Pop the first node in the queue (FIFO)
                cur = queue.popleft()
                current_level.append(cur.val)
                
                # 2. Add children to the queue for the next level
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            # Add the completed level to the final result
            result.append(current_level)
            
        return result
