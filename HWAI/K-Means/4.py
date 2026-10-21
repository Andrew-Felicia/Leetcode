import sys
import math


def e_distance(box1, box2):
    distance = 0.0
    for b1, b2 in zip(box1, box2):
        distance += (b1 - b2) ** 2

    return math.sqrt(distance)
    
def sico(clusters):
    result = []

    for cluster_index, cluster in enumerate(clusters):
        # 题目规定：簇中只有一个点时，该点轮廓系数为 1。
        if len(cluster) <= 1:
            result.append(1.0)
            continue

        point_scores = []

        for point_index, point in enumerate(cluster):
            # a：当前点到“同簇其他点”的平均距离
            same_cluster_distance = 0.0

            for other_index, other_point in enumerate(cluster):
                if point_index == other_index:
                    continue

                same_cluster_distance += e_distance(
                    point,
                    other_point,
                )

            a = same_cluster_distance / (len(cluster) - 1)

            # b：当前点到“其他每个簇”的平均距离中，最小的那个
            b = float("inf")

            for other_cluster_index, other_cluster in enumerate(clusters):
                if other_cluster_index == cluster_index:
                    continue

                # 空簇没有可计算的平均距离，跳过。
                if len(other_cluster) == 0:
                    continue

                other_cluster_distance = 0.0

                for other_point in other_cluster:
                    other_cluster_distance += e_distance(
                        point,
                        other_point,
                    )

                average_distance = (
                    other_cluster_distance / len(other_cluster)
                )

                b = min(b, average_distance)

            # k = 1 时没有其他簇。
            # 此时最终只会输出唯一簇的中心，设为 1.0 不影响选择。
            if b == float("inf"):
                point_scores.append(1.0)
                continue

            # s = (b - a) / max(a, b)
            denominator = max(a, b)

            # 所有点完全重合时，a 和 b 可能都是 0。
            if denominator == 0:
                point_scores.append(0.0)
            else:
                point_scores.append((b - a) / denominator)

        # 当前簇内所有点的 silhouette coefficient 平均值
        result.append(sum(point_scores) / len(point_scores))

    return result




def main():
    data = sys.stdin.readline
    n, k = map(int, data().split())
    boxs = list(list(map(int, data().split())) for _ in range(n))

    centers = boxs[:k]
    clusters_keep = []
    for i in range(100):
        clusters = [[] for _ in range(k)]
        for box in boxs:
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
            box1, box2 = 0.0, 0.0
            for b1, b2 in cluster:
                box1 += b1
                box2 += b2
            new_centers.append([box1 / len(cluster), box2 / len(cluster)])

        distances = 0.0
        for old_center, new_center in zip(centers, new_centers):
            distances += e_distance(old_center, new_center)

        centers = new_centers

        if distances <= 1e-6:
            clusters_keep = clusters
            break

        if i == 99:
            clusters_keep = clusters

    sc = sico(clusters_keep)

    sc_index = sorted(range(len(sc)), key = lambda i : sc[i])[0]

    x, y = centers[sc_index]
    # print(f"{x:.2f}", ",", f"{y:.2f}")
    print(f"{x:.2f},{y:.2f}")

    


        
            




if __name__ == "__main__":
    main()





# if i have a list like : [1,4,2,6,3], i want to get the index of the largest/smallest element, 
# how to solve it using sorted? in python?


# largest_index = sorted(
#     range(len(nums)),
#     key=lambda i: nums[i],
# )[-1]

# smallest_index = sorted(
#     range(len(nums)),
#     key=lambda i: nums[i],
# )[0]

# print(largest_index)   # 3
# print(smallest_index)  # 0