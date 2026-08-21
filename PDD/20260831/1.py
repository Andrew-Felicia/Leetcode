import sys


def minimum_replacements(a, b, maximum):
    parent = list(range(maximum + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    answer = 0
    for x, y in zip(a, b):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y
            answer += 1
    return answer


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    answers = []
    for _ in range(test_cases):
        n, maximum = next(numbers), next(numbers)
        a = [next(numbers) for _ in range(n)]
        b = [next(numbers) for _ in range(n)]
        answers.append(str(minimum_replacements(a, b, maximum)))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
