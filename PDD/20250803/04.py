import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    A = [0] * (n + 1)
    for i in range(1, n + 1):
        A[i] = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))

    INF = float('inf')
    d = [INF] * (n + 1)
    d[1] = 0

    # Nodes are processed in index order, which is a valid topological
    # order since every edge satisfies U_j < V_j.
    for u in range(1, n + 1):
        du = d[u]
        if du == INF:
            continue
        cap = du + A[u]  # max carry achievable leaving u
        for v, w in adj[u]:
            if w <= cap:
                cand = w if w > du else du
                if cand < d[v]:
                    d[v] = cand

    print(d[n] if d[n] != INF else -1)


if __name__ == "__main__":
    solve()