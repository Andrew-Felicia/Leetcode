import sys


def minimum_insertions(values, target):
    answer = 0
    prefix = 0
    seen = {0}
    for value in values:
        prefix += value
        if prefix - target in seen:
            answer += 1
            prefix = value
            seen = {0, prefix}
        else:
            seen.add(prefix)
    return answer


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n, target = numbers[0], numbers[1]
    print(minimum_insertions(numbers[2:2+n], target))


if __name__ == "__main__":
    main()
