import heapq

n = int(input())
heap = []

def main():
    for _ in range(n):
        q = input().split()
        t = int(q[0])

        if t == 1:
            heapq.heappush(heap,int(q[1]))
        elif t == 2:
            print(heap[0])
        elif t == 3:
            heapq.heappop(heap)



if __name__ == '__main__':
    main()



