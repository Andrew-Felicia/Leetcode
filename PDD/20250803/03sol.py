import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    a = [int(x) for x in data[idx:idx + n]]

    # leftreq[j]: minimum value position j must reach so that a[0..j]
    # is strictly increasing (only increments allowed).
    leftreq = [0] * n
    leftreq[0] = a[0]
    for j in range(1, n):
        leftreq[j] = max(a[j], leftreq[j - 1] + 1)

    # rightreq[j]: minimum value position j must reach so that a[j..n-1]
    # is strictly decreasing.
    rightreq = [0] * n
    rightreq[n - 1] = a[n - 1]
    for j in range(n - 2, -1, -1):
        rightreq[j] = max(a[j], rightreq[j + 1] + 1)

    # prefix[j] = total cost to make a[0..j] strictly increasing (via leftreq)
    prefix = [0] * n
    prefix[0] = leftreq[0] - a[0]
    for j in range(1, n):
        prefix[j] = prefix[j - 1] + (leftreq[j] - a[j])

    # suffix[j] = total cost to make a[j..n-1] strictly decreasing (via rightreq)
    suffix = [0] * n
    suffix[n - 1] = rightreq[n - 1] - a[n - 1]
    for j in range(n - 2, -1, -1):
        suffix[j] = suffix[j + 1] + (rightreq[j] - a[j])

    # Try every valid peak position i (1 <= i <= n-2, 0-indexed),
    # i.e. 1 < i < n in 1-indexed terms (interior position).
    best = None
    for i in range(1, n - 1):
        peak_value = max(leftreq[i], rightreq[i])
        cost = prefix[i - 1] + suffix[i + 1] + (peak_value - a[i])
        if best is None or cost < best:
            best = cost

    print(best)


if __name__ == "__main__":
    solve()