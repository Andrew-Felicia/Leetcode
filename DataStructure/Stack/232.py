# class MyQueue:

#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []  #acting like the queue.
        

#     def push(self, x: int) -> None:
#         self.stack1.append(x)

#         #self.stack2 = self.stack1[::-1]

#         # for i in range(len(self.stack1) - 1, -1, -1):
#         #     self.stack2.append(self.stack1[i])

#         while stack
        

#     def pop(self) -> int:
#         return self.stack2[-1]
#         self.stack2 = self.stack2[:-1]
#         #self.stack1 = self.stack2[::-1]

#         # self.stack1 = []
#         # for i in range(len(self.stack2) - 1, -1, -1):
#         #     self.stack1.append(self.stack2[i])
        

#     def peek(self) -> int:
#         return self.stack2[-1]
        

#     def empty(self) -> bool:
#         return len(self.stack2) == 0

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        # Add the new element to the input stack.
        self.input_stack.append(x)

    def _move_elements(self) -> None:
        # Only transfer when output_stack is empty.
        if not self.output_stack:
            while self.input_stack:
                value = self.input_stack.pop()
                self.output_stack.append(value)

    def pop(self) -> int:
        self._move_elements()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move_elements()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()