import heapq
import sys

#Dijkstra’s shortest-path algorithm with two states for every city.
def shortest_cost(n, graph):
    infinity = 10**30
    normal = [infinity] * (n + 1)
    coupon_used = [infinity] * (n + 1)

    normal[1] = 0
    heap = [(0, 1, 0)]  # cost, city, whether the coupon has been used

    while heap:
        cost, city, used = heapq.heappop(heap)
        distances = coupon_used if used else normal

        if cost != distances[city]:
            continue
        if city == n and used:
            return cost

        for next_city, price in graph[city]:
            new_cost = cost + price
            if new_cost < distances[next_city]:
                distances[next_city] = new_cost
                heapq.heappush(heap, (new_cost, next_city, used))

            if not used and cost < coupon_used[next_city]:
                coupon_used[next_city] = cost
                heapq.heappush(heap, (cost, next_city, 1))

    return -1


def solve(data):
    numbers = list(map(int, data.split()))
    n, m = numbers[0], numbers[1]
    graph = [[] for _ in range(n + 1)]

    index = 2
    for _ in range(m):
        u, v, w = numbers[index], numbers[index + 1], numbers[index + 2]
        graph[u].append((v, w))
        index += 3

    return shortest_cost(n, graph)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))