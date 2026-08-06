class TripleInOne:

    def __init__(self, stackSize: int):
        self.stackSize = stackSize
        self.array = [0] * (3 + (stackSize * 3))

    def push(self, stackNum: int, value: int) -> None:
        size = self.array[stackNum]

        if size == self.stackSize:
            return
        index = 3 + self.stackSize * stackNum + size
        self.array[index] = value
        self.array[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        size = self.array[stackNum]

        if size == 0:
            return -1

        index = 3 + self.stackSize * stackNum + size - 1
        self.array[stackNum] -= 1
        return self.array[index]
        

    def peek(self, stackNum: int) -> int:
        size = self.array[stackNum]

        if size == 0:
            return -1

        index = 3 + self.stackSize * stackNum + size - 1
        return self.array[index]
        

    def isEmpty(self, stackNum: int) -> bool:
        return self.array[stackNum] == 0
        


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)