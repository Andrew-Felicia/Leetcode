import sys
from array import array


def main():
    stream = sys.stdin.buffer
    rows, columns = map(int, stream.readline().split())
    relations = int(stream.readline())
    vertices = rows * columns
    head = array("i", [-1]) * (vertices + 1)
    to, following = array("i"), array("i")
    delta_row, delta_column = array("b"), array("b")

    def add_edge(u, v, dr, dc):
        to.append(v)
        delta_row.append(dr)
        delta_column.append(dc)
        following.append(head[u])
        head[u] = len(to) - 1

    offsets = {b"U": (-1, 0), b"B": (1, 0), b"L": (0, -1), b"R": (0, 1)}
    for _ in range(relations):
        a, b, direction = stream.readline().split()
        a, b = int(a), int(b)
        dr, dc = offsets[direction]
        add_edge(b, a, dr, dc)
        add_edge(a, b, -dr, -dc)

    unknown = 2_000_000_000
    row = array("i", [unknown]) * (vertices + 1)
    column = array("i", [unknown]) * (vertices + 1)
    queue = array("i", [0]) * vertices
    row[1] = column[1] = 0
    queue[0] = 1
    front, back = 0, 1
    while front < back:
        u = queue[front]
        front += 1
        edge = head[u]
        while edge != -1:
            v = to[edge]
            if row[v] == unknown:
                row[v] = row[u] + delta_row[edge]
                column[v] = column[u] + delta_column[edge]
                queue[back] = v
                back += 1
            edge = following[edge]

    minimum_row = min(row[1:])
    minimum_column = min(column[1:])
    grid = array("i", [0]) * vertices
    for piece in range(1, vertices + 1):
        r = row[piece] - minimum_row
        c = column[piece] - minimum_column
        grid[r * columns + c] = piece
    output = []
    for r in range(rows):
        output.append(" ".join(map(str, grid[r * columns:(r + 1) * columns])))
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
