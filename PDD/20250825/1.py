import sys


def best_score(bonuses, edge_weights):
    edge_weights.sort()
    total = sum(edge_weights)
    removed = 0
    answer = -10**40
    for components, bonus in enumerate(bonuses, 1):
        if components > 1:
            removed += edge_weights[components - 2]
        answer = max(answer, total - removed + bonus)
    return answer


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    answers = []
    for _ in range(test_cases):
        n = next(numbers)
        bonuses = [next(numbers) for _ in range(n)]
        weights = []
        for _ in range(n - 1):
            next(numbers)
            next(numbers)
            weights.append(next(numbers))
        answers.append(str(best_score(bonuses, weights)))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
