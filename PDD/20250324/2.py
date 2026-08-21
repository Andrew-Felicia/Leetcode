import sys


def game_value(values, m, k, d):
    values.sort(reverse=True)
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)

    n = len(values)
    answer = -10**40
    for removed in range(min(d, n) + 1):
        changed = min(m, n - removed)
        remaining_sum = prefix[n] - prefix[removed]
        changed_sum = prefix[removed + changed] - prefix[removed]
        answer = max(answer, remaining_sum - (k + 1) * changed_sum)
    return answer


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    answers = []
    for _ in range(test_cases):
        n, m, k, d = next(numbers), next(numbers), next(numbers), next(numbers)
        values = [next(numbers) for _ in range(n)]
        answers.append(str(game_value(values, m, k, d)))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
