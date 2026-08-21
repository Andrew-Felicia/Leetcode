import sys


def minimum_deletions(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for left in range(n - 1, -1, -1):
        dp[left][left] = 1
        for right in range(left + 1, n):
            best = 1 + dp[left + 1][right]
            if s[left] == s[left + 1]:
                best = min(best, 1 + (dp[left + 2][right] if left + 2 <= right else 0))
            for partner in range(left + 2, right + 1):
                if s[left] == s[partner]:
                    middle = dp[left + 1][partner - 1]
                    tail = dp[partner + 1][right] if partner < right else 0
                    best = min(best, middle + tail)
            dp[left][right] = best
    return dp[0][n - 1]


def main():
    tokens = sys.stdin.buffer.read().split()
    test_cases = int(tokens[0])
    print("\n".join(str(minimum_deletions(tokens[i].decode()))
                    for i in range(1, test_cases + 1)))


if __name__ == "__main__":
    main()
