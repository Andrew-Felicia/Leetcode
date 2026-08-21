import sys


def maximum_activated(points):
    n = len(points)
    graph = [[] for _ in range(n)]
    for i, (x, y, radius) in enumerate(points):
        for j, (other_x, other_y, _) in enumerate(points):
            if i != j and (x - other_x) ** 2 + (y - other_y) ** 2 <= radius ** 2:
                graph[i].append(j)

    answer = 0
    for start in range(n):
        seen = {start}
        stack = [start]
        while stack:
            user = stack.pop()
            for neighbor in graph[user]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        answer = max(answer, len(seen))
    return answer


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    answers = []
    for _ in range(test_cases):
        n = next(numbers)
        points = [(next(numbers), next(numbers), next(numbers)) for _ in range(n)]
        answers.append(str(maximum_activated(points)))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
