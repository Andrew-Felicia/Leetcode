import sys


def available_time(total, intervals):
    intervals.sort()
    blocked = 0
    left, right = intervals[0]
    for start, end in intervals[1:]:
        if start <= right:
            right = max(right, end)
        else:
            blocked += right - left + 1
            left, right = start, end
    blocked += right - left + 1
    return total - blocked


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    answers = []
    for _ in range(test_cases):
        total, n = next(numbers), next(numbers)
        intervals = [(next(numbers), next(numbers)) for _ in range(n)]
        answers.append(str(available_time(total, intervals)))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
