import sys


def minimum_distance(n, limit, parent):
    children = [[] for _ in range(n)]
    depth = [0] * n
    for node in range(1, n):
        children[parent[node]].append(node)
        depth[node] = depth[parent[node]] + 1

    levels = max(1, n.bit_length())
    up = [parent[:]]
    for _ in range(1, levels):
        previous = up[-1]
        up.append([previous[previous[node]] for node in range(n)])

    tin = [0] * n
    tout = [0] * n
    order = []
    stack = [(0, 0)]
    while stack:
        node, state = stack.pop()
        if state == 0:
            tin[node] = len(order)
            order.append(node)
            stack.append((node, 1))
            for child in reversed(children[node]):
                stack.append((child, 0))
        else:
            tout[node] = len(order) - 1
    deepest_first = sorted(range(n), key=depth.__getitem__, reverse=True)

    def feasible(distance):
        bit = [0] * (n + 2)
        def add(index, value):
            index += 1
            while index < len(bit):
                bit[index] += value
                index += index & -index
        def covered(index):
            index += 1
            total = 0
            while index:
                total += bit[index]
                index -= index & -index
            return total > 0
        used = 0
        for node in deepest_first:
            if covered(tin[node]):
                continue
            center = node
            jump = distance
            bit_index = 0
            while jump:
                if jump & 1:
                    center = up[bit_index][center]
                jump >>= 1
                bit_index += 1
            used += 1
            if used > limit:
                return False
            add(tin[center], 1)
            add(tout[center] + 1, -1)
        return True

    low, high = 0, max(depth)
    while low < high:
        middle = (low + high) // 2
        if feasible(middle):
            high = middle
        else:
            low = middle + 1
    return low


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    test_cases = next(numbers)
    answers = []
    for _ in range(test_cases):
        n, limit = next(numbers), next(numbers)
        parent = [0] + [next(numbers) - 1 for _ in range(n - 1)]
        answers.append(str(minimum_distance(n, limit, parent)))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
