class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        tmp = Stack()
        for i in s:
            if i == "(" or i == "[" or i == "{":
                tmp.push(i)
            elif(tmp.size() == 0):
                return False
            elif( (i == ")" and tmp.peek() == "(") or (i == "]" and tmp.peek() == "[") or
                  (i == "}" and tmp.peek() == "{" ) ):
                tmp.pop()
            else:
                return False
        return tmp.size() == 0