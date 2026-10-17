import sys
import math


# In Python, 1e-10 is the scientific notation for a floating-point number representing 1 × 10⁻¹⁰,
#     which is 0.0000000001

# The core difference is that list.sort() modifies the original list in-place and returns None, 
# whereas the sorted() function returns a new sorted list leaving the original data unchanged.

# numbers = [5, 2, 8, 1]

# # Mutates numbers directly, returns None
# result = numbers.sort() 

# print(numbers) # Output: [1, 2, 5, 8]
# print(result)  # Output: None

# numbers_tuple = (5, 2, 8, 1)

# # Leaves numbers_tuple intact, returns a new sorted list
# new_list = sorted(numbers_tuple)

# print(numbers_tuple) # Output: (5, 2, 8, 1)
# print(new_list)      # Output: [1, 2, 5, 8]


# >>> 0.11+0.29
# 0.39999999999999997

def t_distance(t1, t2):
    d = 0.0
    for x, y in zip(t1, t2):
        d += (x - y) ** 2
    return math.sqrt(d)


def main():
    data = sys.stdin.buffer.readline
    k, m, n = list(map(int, data().split()))
    samples = []
    for _ in range(m):
        samples.append(list(map(float, data().split())))

    centers = samples[:k]

    for _ in range(n):
        clusters = [[] for _ in range(k)]    #remember to put inside the itreation.
        for sample in samples:
            min_distance = t_distance(sample, centers[0])
            min_index = 0
            for index, center in enumerate(centers[1:], start = 1):
                distance = t_distance(sample, center)
                if distance < min_distance:
                    min_distance = distance
                    min_index = index
            clusters[min_index].append(sample)

        new_centers = []
        for cluster in clusters:
            sum_a, sum_b, sum_c, sum_d = 0.0, 0.0, 0.0, 0.0
            for a, b, c, d in cluster:
                sum_a += a
                sum_b += b
                sum_c += c
                sum_d += d
            new_centers.append([sum_a / len(cluster), sum_b / len(cluster), 
                                sum_c / len(cluster), sum_d / len(cluster)])

        center_distances = 0.0
        for old_center, new_center in zip(centers, new_centers):
            center_distances += t_distance(old_center, new_center)

        if center_distances < 1e-8:
            break

        centers = new_centers


    result = []
    # clusters.sort(key = lambda cluster: len(cluster))
    for cluster in clusters:
        result.append(len(cluster))
    result.sort()
    print(*result)







    


if __name__ == "__main__":
    main()