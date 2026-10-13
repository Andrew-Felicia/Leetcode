import sys
import math

# >>> s = [6,1,3,2]
# >>> s
# [6, 1, 3, 2]
# >>> sorted(range(4), key = lambda i:(s[i], i))
# [1, 3, 2, 0]
# >>> sorted(range(4), key = lambda i:s[i])
# [1, 3, 2, 0]


# data = [10, 50, 30, 20]

# # Use max() on enumerated data to get the index
# argmax_index = max(range(len(data)), key=lambda i: data[i])
# print(argmax_index)  # Output: 1

# # Alternative using enumerate()
# argmax_index_alt = max(enumerate(data), key=lambda x: x[1])[0]
# print(argmax_index_alt)  # Output: 1

# import pandas as pd

# series = pd.Series([10, 50, 30, 20], index=['a', 'b', 'c', 'd'])

# print(series.idxmax())  # Output: 'b' (Returns the row label)
# print(series.argmax())  # Output: 1   (Returns the integer position)



def main():
    data = sys.stdin.readline
    n, d, c = map(int, data().split())
    x = list(list(map(float, data().split())) for _ in range(n))
    w = list(list(map(float, data().split())) for _ in range(d))
    ratio = float(data())

    # print(n, d, c)
    # print(x)
    # print(w)
    # print(ratio)
    k = math.floor(ratio * d)
    if ratio > 0 and k == 0:
        k = 1

    w_sum = [sum(abs(value) for value in row) for row in w]

    to_be_removed_row_index = set(sorted(range(d), key = lambda i : w_sum[i])[:k])
    #print(to_be_removed_row_index)

    answer = []
    for row in range(n):
        line = []
        for col in range(c):
            scores = 0
            for i in range(d):
                if i in to_be_removed_row_index:
                    continue
                scores += x[row][i] * w[i][col]
            line.append(scores)
        answer.append(max(range(len(line)), key = lambda i : line[i]))
    print(*answer)
                



    





if __name__ == "__main__":
    main()