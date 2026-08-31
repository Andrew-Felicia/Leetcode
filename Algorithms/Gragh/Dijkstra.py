import heapq

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 1), ("E", 5)],
    "C": [("A", 2), ("D", 4)],
    "D": [("B", 1), ("C", 4), ("E", 2)],
    "E": [("B", 5), ("D", 2)],
}
#       4
#   A ──── B
#   │      │ \
# 2 │    1 │  \ 5
#   │      │   \
#   C ──── D ─── E
#       4      2


def dijkstra(graph, start, target):
    distance = {node:float('inf') for node in graph}
    previous = {node:None for node in graph}

    distance[start] = 0
    heap = [(0, start)]

    while heap:
        cur_distance, cur_node = heapq.heappop(heap)

        if cur_distance > distance[cur_node]:
            continue
        if cur_node == target:
            break
        for neighbor, weight in graph[cur_node]:
            new_distance = cur_distance + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                previous[neighbor] = cur_node
                heapq.heappush(heap, (new_distance, neighbor))

    path = []
    node = target
    while node:
        path.append(node)
        node = previous[node]
    path.reverse()

    return distance[target], path


distance, path = dijkstra(graph, "A", "E")
print("distance: ", distance)
print("path: ", " -> ".join(path))
