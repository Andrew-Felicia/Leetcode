import sys

def has_distinct_digits(x):
    s = str(x)
    return len(set(s)) == len(s)

def solve():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    results = []

    for _ in range(T):
        n = int(data[idx]); idx += 1
        candidate = n + 1
        while not has_distinct_digits(candidate):
            candidate += 1
        results.append(str(candidate))

    print('\n'.join(results))


if __name__ == "__main__":
    solve()