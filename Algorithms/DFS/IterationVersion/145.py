class Solution:
    def postorderTraversal(self, root):
        stack = []
        result = []
        cur = root
        
        while cur or stack:
            # 1. Reach the right-most node (instead of left)
            while cur:
                result.append(cur.val) # Process Root
                stack.append(cur)
                cur = cur.right        # Move Right first
            
            # 2. Backtrack and move to the Left child
            cur = stack.pop()
            cur = cur.left             # Move Left last
            
        # 3. Reverse the result to turn Root-Right-Left into Left-Right-Root
        return result[::-1]
    


class Solution:
    def postorderTraversal(self, root):
        stack = []
        result = []
        cur = root
        last_visited = None
        
        while cur or stack:
            # 1. Reach the left-most node
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # Peek the top of the stack
            peek_node = stack[-1]
            
            # 2. Check if we should move to the right child or process this node
            # If the right child exists and hasn't been visited yet, go right
            if peek_node.right and last_visited != peek_node.right:
                cur = peek_node.right
            else:
                # 3. Both children are processed, visit the root/parent
                result.append(peek_node.val)
                last_visited = stack.pop()
                # 'cur' remains None to continue popping from stack in next iteration
                
        return result



