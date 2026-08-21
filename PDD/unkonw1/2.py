import sys


def maximum_tasks(tasks, token_budget, time_budget):
    dp = [[-100] * (time_budget + 1) for _ in range(token_budget + 1)]
    dp[0][0] = 0
    for a, b, c, d in tasks:
        old = [row[:] for row in dp]
        for tokens in range(token_budget + 1):
            for time in range(time_budget + 1):
                if old[tokens][time] < 0:
                    continue
                if tokens + a <= token_budget and time + b <= time_budget:
                    dp[tokens + a][time + b] = max(dp[tokens + a][time + b], old[tokens][time] + 1)
                if tokens + c <= token_budget and time + d <= time_budget:
                    dp[tokens + c][time + d] = max(dp[tokens + c][time + d], old[tokens][time] + 1)
    return max(map(max, dp))


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    n, token_budget, time_budget = next(numbers), next(numbers), next(numbers)
    tasks = [(next(numbers), next(numbers), next(numbers), next(numbers)) for _ in range(n)]
    print(maximum_tasks(tasks, token_budget, time_budget))


if __name__ == "__main__":
    main()
