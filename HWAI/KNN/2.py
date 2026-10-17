import sys
import math

def main():
    data = sys.stdin.readline
    n, k = list(map(int, data().split()))
    samples = []
    for _ in range(n):
        index = 0
        sample = data().split()
        samples.append([float(sample[index]), float(sample[index + 1]), 
                              float(sample[index + 2]), int(sample[index + 3])])
        index += 4
    target = list(map(float, data().split()))

    neighbors = []
    for sample in samples:
        label = sample[3]
        distance = 0.0
        difference = 0.0
        for s, t in zip(sample, target):
            difference += (s - t) ** 2
        distance = math.sqrt(difference)

        neighbors.append((label, distance))
    neighbors.sort(key = lambda elem : elem[1])

    result = neighbors[:k]

    label_counts = {}   # label : counts
    for l, d in result:
        label_counts[l] = label_counts.get(l, 0) + 1
    max_counts = max(label_counts.values())

    label_answer = 0
    for l, c in label_counts.items():
        if c == max_counts:
            label_answer = l
            break

    print(label_answer)










            



if __name__ == "__main__":
    main()