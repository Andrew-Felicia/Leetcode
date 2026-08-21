import sys


def distinct_digits(number):
    text = str(number)
    return len(text) == len(set(text))


def next_password(number):
    candidate = number + 1
    while not distinct_digits(candidate):
        candidate += 1
    return candidate


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    print("\n".join(str(next_password(next(numbers))) for _ in range(test_cases)))


if __name__ == "__main__":
    main()
