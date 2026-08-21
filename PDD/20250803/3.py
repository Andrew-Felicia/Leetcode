import sys


def minimum_increments(a):
    n = len(a)
    left = [0] * n
    right = [0] * n
    left[0] = a[0]
    for i in range(1, n):
        left[i] = max(a[i], left[i - 1] + 1)
    right[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        right[i] = max(a[i], right[i + 1] + 1)

    prefix = [0] * n
    suffix = [0] * n
    for i in range(n):
        prefix[i] = (prefix[i - 1] if i else 0) + left[i] - a[i]
    for i in range(n - 1, -1, -1):
        suffix[i] = (suffix[i + 1] if i + 1 < n else 0) + right[i] - a[i]

    answer = 10**30
    for peak in range(1, n - 1):
        cost = prefix[peak - 1] + suffix[peak + 1]
        cost += max(left[peak], right[peak]) - a[peak]
        answer = min(answer, cost)
    return answer


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    print(minimum_increments(numbers[1:1 + numbers[0]]))


if __name__ == "__main__":
    main()
