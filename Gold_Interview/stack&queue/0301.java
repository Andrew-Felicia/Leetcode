
class TripleInOne {
    private final int stackSize;
    private final int[] array;

    public TripleInOne(int stackSize) {
        this.stackSize = stackSize;
        this.array = new int[3 + 3 * stackSize];
    }
    
    public void push(int stackNum, int value) {
        int size = this.array[stackNum];
        if (size == this.stackSize) {
            return;
        }
        int index = 3 + stackNum * this.stackSize + size;
        this.array[index] = value;
        this.array[stackNum] += 1;
        return;
    }
    
    public int pop(int stackNum) {
        int size = this.array[stackNum];
        if (size == 0) {
            return -1;
        }
        int index = 3 + stackNum * this.stackSize + size - 1;
        this.array[stackNum] -= 1;
        return this.array[index];
    }
    
    public int peek(int stackNum) {
        int size = this.array[stackNum];
        if (size == 0) {
            return -1;
        }
        int index = 3 + stackNum * this.stackSize + size - 1;
        return this.array[index];
    }
    
    public boolean isEmpty(int stackNum) {
        return this.array[stackNum] == 0;
    }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * TripleInOne obj = new TripleInOne(stackSize);
 * obj.push(stackNum,value);
 * int param_2 = obj.pop(stackNum);
 * int param_3 = obj.peek(stackNum);
 * boolean param_4 = obj.isEmpty(stackNum);
 */