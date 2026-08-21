import sys


def is_sorted(values):
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


def minimum_swaps(values, held):
    inversions = sum(values[i] > values[i + 1] for i in range(len(values) - 1))
    if inversions == 0:
        return 0
    operations = 0
    for i in range(len(values) - 1, -1, -1):
        if values[i] < held and (i + 1 == len(values) or held <= values[i + 1]):
            if i > 0:
                inversions -= values[i - 1] > values[i]
            if i + 1 < len(values):
                inversions -= values[i] > values[i + 1]
            values[i], held = held, values[i]
            if i > 0:
                inversions += values[i - 1] > values[i]
            if i + 1 < len(values):
                inversions += values[i] > values[i + 1]
            operations += 1
            if inversions == 0:
                return operations
    return -1


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    answers = []
    for _ in range(test_cases):
        n, held = next(numbers), next(numbers)
        answers.append(str(minimum_swaps([next(numbers) for _ in range(n)], held)))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
