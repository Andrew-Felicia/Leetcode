import sys
import math
import heapq


def main():
    data = sys.stdin.readline
    n, d = map(int, data().split())
    tokens = []
    for _ in range(n):
        tokens.append(list(map(float, data().split())))
    limits = list(map(int, data().split()))

    # print(n, d)
    # print(tokens)
    # print(limits)

    normalized_tokens = [[0.0] * d for _ in range(n)]
    for index, token in enumerate(tokens):
        norm = 0.0
        for value in token:
            norm += value * value
        norm = math.sqrt(norm / d)
        normalized_tokens[index] = [value / norm for value in token]
    # print(normalized_tokens)

    total_scores = 0.0
    for i in range(1, n):
        limit = min(i, limits[i])
        if limit == 0:
            continue
        score = []
        target = normalized_tokens[i]
        for j in range(i):
            dot_prouct = 0.0
            source = normalized_tokens[j]
            for feature in range(d):
                dot_prouct += target[feature] * source[feature]
            score.append((dot_prouct / math.sqrt(d)) ** 2)

        if limit == i:
            total_scores += sum(score)
        else:
            total_scores += sum(heapq.nlargest(limit, score))

    print(round(total_scores * 100))




    





if __name__ == "__main__":
    main()