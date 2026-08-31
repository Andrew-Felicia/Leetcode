Here’s a simple example of **Dijkstra’s algorithm** for finding the shortest weighted path.

### Example graph

```text
      4
  A ──── B
  │      │ \
2 │    1 │  \ 5
  │      │   \
  C ──── D ─── E
      3      2
```

Edges:

- A–B: 4
- A–C: 2
- B–D: 1
- B–E: 5
- C–D: 3
- D–E: 2

Find the shortest path from **A to E**.

### Dijkstra’s steps

| Visited node | Best distances from A |
|---|---|
| Start | A=0, B=∞, C=∞, D=∞, E=∞ |
| A | B=4, C=2 |
| C | D=5 |
| B | D=5, E=9 |
| D | E=7 |
| E | Finished |

The shortest distance is **7**. Two paths have this distance:

```text
A → B → D → E
4 + 1 + 2 = 7
```

```text
A → C → D → E
2 + 3 + 2 = 7
```

### Python implementation

```python
import heapq

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 1), ("E", 5)],
    "C": [("A", 2), ("D", 3)],
    "D": [("B", 1), ("C", 3), ("E", 2)],
    "E": [("B", 5), ("D", 2)],
}


def dijkstra(graph, start, target):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Ignore outdated queue entries
        if current_distance > distances[current_node]:
            continue

        if current_node == target:
            break

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))

    # Reconstruct one shortest path
    path = []
    node = target

    while node is not None:
        path.append(node)
        node = previous[node]

    path.reverse()
    return distances[target], path


distance, path = dijkstra(graph, "A", "E")

print("Shortest distance:", distance)
print("Path:", " → ".join(path))
```

Output:

```text
Shortest distance: 7
Path: A → B → D → E
```

Dijkstra’s algorithm requires all edge weights to be **non-negative**. Its typical time complexity with a priority queue is `O((V + E) log V)`.