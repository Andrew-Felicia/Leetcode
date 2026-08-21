import sys
from collections import deque


def minimum_walks(teleport):
    n = len(teleport) - 1
    distance = [n + 1] * (n + 1)
    distance[1] = 0
    queue = deque([1])
    while queue:
        u = queue.popleft()
        v = teleport[u]
        if distance[u] < distance[v]:
            distance[v] = distance[u]
            queue.appendleft(v)
        for v in (u - 1, u + 1):
            if 1 <= v <= n and distance[u] + 1 < distance[v]:
                distance[v] = distance[u] + 1
                queue.append(v)
    return distance[1:]


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    print(*minimum_walks([0] + numbers[1:1+n]))


if __name__ == "__main__":
    main()
