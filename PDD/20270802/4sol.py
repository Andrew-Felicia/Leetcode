import sys


def minimum_rounds(a):
    n = len(a)

    if n == 1:
        return a[0]

    answer = max(a[i] + a[(i + 1) % n] for i in range(n))

    if n % 2 == 1:
        maximum_per_round = n // 2
        total_bound = (sum(a) + maximum_per_round - 1) // maximum_per_round
        answer = max(answer, total_bound)

    return answer


def solve(data):
    numbers = iter(map(int, data.split()))
    test_cases = next(numbers)
    answers = []

    for _ in range(test_cases):
        n = next(numbers)
        a = [next(numbers) for _ in range(n)]
        answers.append(str(minimum_rounds(a)))

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))