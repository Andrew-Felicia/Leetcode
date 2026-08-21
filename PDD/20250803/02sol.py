import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    results = []

    for _ in range(T):
        n = int(data[idx]); idx += 1
        pts = []
        for _ in range(n):
            x = int(data[idx]); y = int(data[idx + 1]); r = int(data[idx + 2])
            idx += 3
            pts.append((x, y, r))

        # Build directed adjacency: edge i -> j if dist(i, j) <= r_i
        # Use squared distances to avoid floating point issues.
        adj = [[] for _ in range(n)]
        for i in range(n):
            xi, yi, ri = pts[i]
            ri2 = ri * ri
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = pts[j]
                dx = xi - xj
                dy = yi - yj
                if dx * dx + dy * dy <= ri2:
                    adj[i].append(j)

        # For each possible starting node, BFS/DFS to find reachable set size.
        best = 0
        for s in range(n):
            visited = [False] * n
            visited[s] = True
            stack = [s]
            count = 1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        count += 1
                        stack.append(v)
            best = max(best, count)

        results.append(str(best))

    print('\n'.join(results))


if __name__ == "__main__":
    solve()