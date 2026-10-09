#cosine similarity
# vec1 = [1, 2, 3]
# vec2 = [4, 5, 6]

# # Calculate dot product
# dot_product = sum(a * b for a, b in zip(vec1, vec2))

# # Calculate magnitudes (norms)
# norm_vec1 = sum(a * a for a in vec1) ** 0.5
# norm_vec2 = sum(b * b for b in vec2) ** 0.5

# # Avoid DivisionByZero if a vector is empty/zero
# if norm_vec1 == 0 or norm_vec2 == 0:
#     similarity = 0.0
# else:
#     similarity = dot_product / (norm_vec1 * norm_vec2)

# print(f"Similarity: {similarity:.4f}")
# # Output: Similarity: 0.9746

import sys
import math

class Union:
    def __init__(self, n):
        #for parent[i], i is the item, and parent[i] is i's parent.
        self.parent = list(range(n))
        #for size[i], i is the root of a disjoint set(whose parent is itself), size[i] is the size of this disjoint set.
        self.size = [1] * n

    #find the representative of this disjoint set, whose parent is itself.
    def find(self, x):
        # if self.parent[x] == x:
        #     return x
        # return self.find(self.parent[x])

        #path compression
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    #union two item to one cluster. if they aleady in the same cluster, return the size of this cluster. otherwise, union them first
    #and return the size of the unioned cluster.
    def union(self, a, b):
        # root_a = self.find(a)
        # root_b = self.find(b)
        # if root_a == root_b:
        #     return self.size(root_a)

        # self.parent[root_b] = root_a
        # self.size[root_a] += self.size[root_b]

        # return self.size[root_a]

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
    lines = [line.split() for line in sys.stdin.buffer.readlines() if line.strip()]

    if len(lines) == 0:
        print(0)
        return

    vectors = []
    dimensions = 0

    for parts in lines:
        if len(parts) < 2:
            print(0)
            return
        vector = list(map(float, parts[1:]))
        if dimensions == 0:
            dimensions = len(vector)
        elif dimensions != len(vector):
            print(0)
            return
        vectors.append(vector)

    normalized_vectors = []
    #normalization
    for vector in vectors:
        norm = math.sqrt(sum(elem * elem for elem in vector))
        if norm == 0:
            normalized_vectors.append(None)
        normalized_vectors.append([elem / norm for elem in vector])

    n = len(vectors)
    largest_cluster = 1
    union_find = Union(n)
    for i in range(n):
        if normalized_vectors[i] == None:
            continue
        for j in range(i + 1, n):
            if normalized_vectors[j] == None:
                continue

            similarity = sum(normalized_vectors[i][k] * normalized_vectors[j][k] 
                             for k in range(dimensions))
            if similarity >= 0.95:
                largest_cluster = max(largest_cluster, union_find.union(i, j))


    print(largest_cluster)



    
if __name__ == "__main__":
    main()