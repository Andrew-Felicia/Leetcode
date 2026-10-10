# import heapq

# tasks = []

# # Tuple format: (priority_number, task_name)
# heapq.heappush(tasks, (3, "Write documentation"))
# heapq.heappush(tasks, (1, "Fix critical bug"))
# heapq.heappush(tasks, (2, "Review PRs"))

# # The lowest priority number gets popped first
# while tasks:
#     priority, task = heapq.heappop(tasks)
#     print(f"Executing: {task} (Priority {priority})")
    
# # Output:
# # Executing: Fix critical bug (Priority 1)
# # Executing: Review PRs (Priority 2)
# # Executing: Write documentation (Priority 3)



import sys
import heapq




def main():
    data = sys.stdin.buffer.readline
    n = int(data())
    m = int(data())
    samples = list(map(int, data().split()))

    samples.sort(reverse = True)

    npu_heap = [(0, i) for i in range(n)] #(priority number, npu index)
    heapq.heapify(npu_heap)

    for sample in samples:
        p, n = heapq.heappop(npu_heap)
        p += sample
        heapq.heappush(npu_heap, (p, n))

    result = max(npu_heap, key=lambda i : i[0])
    print(result[0])



if __name__ == "__main__":
    main()