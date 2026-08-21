import sys
from collections import deque


def count_super_nodes(n, edges):
    graph = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        reverse[v].append(u)
        indegree[v] += 1

    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    prefix_ok = [False] * n
    outgoing_inside = [0] * n
    sinks = 0
    for u in order:
        sinks += 1
        for predecessor in reverse[u]:
            if outgoing_inside[predecessor] == 0:
                sinks -= 1
            outgoing_inside[predecessor] += 1
        prefix_ok[u] = sinks == 1

    suffix_ok = [False] * n
    incoming_inside = [0] * n
    sources = 0
    for u in reversed(order):
        sources += 1
        for successor in graph[u]:
            if incoming_inside[successor] == 0:
                sources -= 1
            incoming_inside[successor] += 1
        suffix_ok[u] = sources == 1

    return sum(prefix_ok[u] and suffix_ok[u] for u in range(n))


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]
    edges = [(data[i] - 1, data[i + 1] - 1) for i in range(2, 2 + 2 * m, 2)]
    print(count_super_nodes(n, edges))


if __name__ == "__main__":
    main()
