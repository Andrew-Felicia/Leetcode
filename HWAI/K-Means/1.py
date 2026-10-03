import sys

def d_distance(box1, box2):
    w1, h1 = box1
    w2, h2 = box2
    intersection = min(w1, w2) * min(h1, h2)
    union = w1 * h1 + w2 * h2 - intersection
    return 1 - intersection / (union + 1e-16)

def main():
    input = sys.stdin.buffer.readline
    N, K, T = map(int, input().split())
    boxs = []
    for _ in range(N):
        boxs.append(tuple(map(int, input().split())))

    #print(boxs)
    centers = boxs[:K]
    


    for _ in range(T):
        clusters = [[] for _ in range(K)]
        for box in boxs:
            min_distance = d_distance(box, centers[0])
            min_distance_index = 0
            for index, center in enumerate(centers[1:], start = 1):
                distance = d_distance(box, center)
                if distance < min_distance:
                    min_distance = distance
                    min_distance_index = index
                
            clusters[min_distance_index].append(box)

        new_centers = []
        for cluster in clusters:
            width = sum(box[0] for box in cluster)
            height = sum(box[1] for box in cluster)
            new_centers.append((width // len(cluster), height // len(cluster)))

        distances = 0
        for old_box, new_box in zip(centers, new_centers):
            distances += d_distance(old_box, new_box)

        centers = new_centers

        if distances < 1e-4:
            break

    centers = sorted(centers, key = lambda box : box[0] * box[1], reverse = True)
    for center in centers:
        print(center[0], center[1])



if __name__ == "__main__":
    main()
