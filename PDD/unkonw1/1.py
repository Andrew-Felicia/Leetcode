import heapq
import sys


def maximum_matches(intervals, slots):
    intervals.sort()
    slots.sort()
    heap = []
    index = 0
    answer = 0
    for slot in slots:
        while index < len(intervals) and intervals[index][0] <= slot:
            heapq.heappush(heap, intervals[index][1])
            index += 1
        while heap and heap[0] < slot:
            heapq.heappop(heap)
        if heap:
            heapq.heappop(heap)
            answer += 1
    return answer


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    answers = []
    for _ in range(test_cases):
        n, m = next(numbers), next(numbers)
        intervals = [(next(numbers), next(numbers)) for _ in range(n)]
        slots = [next(numbers) for _ in range(m)]
        answers.append(str(maximum_matches(intervals, slots)))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
