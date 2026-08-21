import sys


def minimum_difficulty(scores, difficulties, target):
    def feasible(limit):
        current = 0
        for score, difficulty in zip(scores, difficulties):
            current = current + score if difficulty <= limit else 0
            if current >= target:
                return True
        return False

    low, high = min(difficulties), max(difficulties)
    while low < high:
        middle = (low + high) // 2
        if feasible(middle):
            high = middle
        else:
            low = middle + 1
    return low


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    n, target = next(numbers), next(numbers)
    scores, difficulties = [], []
    for _ in range(n):
        scores.append(next(numbers))
        difficulties.append(next(numbers))
    print(minimum_difficulty(scores, difficulties, target))


if __name__ == "__main__":
    main()
