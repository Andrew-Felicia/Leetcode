import sys


NOISE = -1
UNVISITED = -2

def distance(point1, point2):
    distances = 0.0
    for p1, p2 in zip(point1, point2):
        distances += (p1 - p2) ** 2
    return distances



def dbscan(eps, min_samples, points):
    n = len(points)
    labels = [UNVISITED] * n
    cluster_count = 0
    eps_squared = eps * eps

    def find_neighbors(index):
        neighbors = []

        for neighbor_index in range(n):
            # if neighbor_index == index:
            #     continue
            if distance(points[index], points[neighbor_index]) < eps_squared:
                neighbors.append(neighbor_index)

        return neighbors

    for index in range(n):
        #if this point is been processed, then skip.
        if labels[index] != UNVISITED:
            continue
        neighbors = find_neighbors(index)

        if len(neighbors) <= min_samples:
            labels[index] = NOISE
            continue

        labels[index] = cluster_count

        queue = neighbors[:]
        queued = set(queue)

        head = 0

        while head < len(queue):
            current_index = queue[head]
            head += 1

            if labels[current_index] == NOISE:
                labels[current_index] = cluster_count

            if labels[current_index] != UNVISITED:
                continue


            # current_index is either core point or non-core point
            labels[current_index] = cluster_count

            current_neighbors = find_neighbors(current_index)

            if len(current_neighbors) > min_samples:
                for neighbor_index in current_neighbors:
                    if (
                        labels[neighbor_index] 
                        in (UNVISITED, NOISE)
                        and neighbor_index not in queued
                    ):
                        queue.append(neighbor_index)
                        queued.add(neighbor_index)

        cluster_count += 1

    noise_count = sum(
        1 for node in labels if node == NOISE
    )

    return cluster_count, noise_count
                        
def main():
    data = sys.stdin.readline
    eps, min_samples, x = list(data().split())
    eps = float(eps)
    min_samples = int(min_samples)
    x = int(x)

    points = list(list(map(float, data().split())) for _ in range(x))

    cluster_count, noise_count = dbscan(eps, min_samples, points)

    print(cluster_count, noise_count)



if __name__ == "__main__":
    main()