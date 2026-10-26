import sys

class Union:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return self.size[root_a]
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        return self.size[root_a]


def main():
    input = sys.stdin.readline
    n = int(input())
    uf = Union(n)

    data = list(list(input().split()) for _ in range(n))

    #print(n, data)

    row_recorder = {}  # number : row index

    for row in range(n):
        for i in data[row]:
            if i in row_recorder:
                uf.union(row, row_recorder[i])
            else:
                row_recorder[i] = row

    merged = {}

    for i, v in enumerate(data):
        root = uf.find(i)
        if root not in merged:
            merged[root] = set()
        merged[root].update(v)

    result = [sorted(i) for i in merged.values()]

    result.sort()


    for i in result:
        print(*i)





if __name__ == "__main__":
    main()