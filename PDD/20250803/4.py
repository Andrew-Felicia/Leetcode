import sys


def minimum_packages(n, supplies, graph):
    infinity = 10**30
    need = [infinity] * (n + 1)
    need[1] = 0
    for u in range(1, n + 1):
        if need[u] == infinity:
            continue
        capacity = need[u] + supplies[u]
        for v, required in graph[u]:
            if required <= capacity:
                need[v] = min(need[v], max(need[u], required))
    return -1 if need[n] == infinity else need[n]


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(numbers), next(numbers)
    supplies = [0] + [next(numbers) for _ in range(n)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = next(numbers), next(numbers), next(numbers)
        graph[u].append((v, w))
    print(minimum_packages(n, supplies, graph))


if __name__ == "__main__":
    main()
