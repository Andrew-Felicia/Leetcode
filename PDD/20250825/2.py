import sys


def minimum_operations(values):
    even_count = sum(value % 2 == 0 for value in values)
    if even_count < len(values):
        return even_count

    minimum_halves = 100
    for value in values:
        halves = 0
        while value % 2 == 0:
            value //= 2
            halves += 1
        minimum_halves = min(minimum_halves, halves)
    return len(values) - 1 + minimum_halves


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    answers = []
    for _ in range(test_cases):
        n = next(numbers)
        answers.append(str(minimum_operations([next(numbers) for _ in range(n)])))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
