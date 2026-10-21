import sys
import math


def e_distance(box1, box2):
    distance = 0.0
    for b1, b2 in zip(box1, box2):
        distance += (b1 - b2) ** 2
    return math.sqrt(distance)



def main():
    data = sys.stdin.readline
    k = int(data())
    centers = list(list(map(float, data().split())) for _ in range(k))
    t = int(data())
    m = int(data())
    samples = list(list(map(float, data().split())) for _ in range(m))

    boxs = centers + samples

    for _ in range(t):
        clusters = [[] for _ in range(k)]
        for box in samples:                                #attention! not for box in boxs: because the 
                                                           #initial centers are already included inside the samples.
            min_distance = e_distance(box, centers[0])
            min_index = 0
            for index, center in enumerate(centers[1:], start = 1):
                distance = e_distance(center, box)
                if distance < min_distance:
                    min_distance = distance
                    min_index = index
            clusters[min_index].append(box)

        new_centers = []
        for cluster in clusters:
            box1, box2, box3 = 0.0, 0.0, 0.0
            for b1, b2, b3 in cluster:
                box1 += b1
                box2 += b2
                box3 += b3

            new_centers.append([box1 / len(cluster), box2 / len(cluster), box3 / len(cluster)])


        centers = new_centers

    #if it's zero, it will trucate.
    #ex: 35.0 instead of 35.00
    # for center in centers:
    #     center[0], center[1], center[2] = round(center[0], 2), round(center[1], 2), round(center[2], 2)


    for center in centers:
        print(
            f"{center[0]:.2f}",
            f"{center[1]:.2f}",
            f"{center[2]:.2f}"
        )


if __name__ == "__main__":
    main()