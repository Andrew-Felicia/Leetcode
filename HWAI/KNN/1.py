import sys

def main():
    #Read everything until the terminal sends EOF.
    # Pressing Enter or adding blank lines does not send EOF. On macOS, after the final input line, press:
    # Ctrl+D
    # You pressed Ctrl+C, which cancels the program and causes KeyboardInterrupt
    data = sys.stdin.buffer.read().split()
    index = 0
    k = int(data[index])
    m = int(data[index + 1])
    n = int(data[index + 2])
    s = int(data[index + 3])

    index += 4

    target = []
    for _ in range(n):
        target.append(float(data[index]))
        index += 1

    distances = []
    for i in range(m):
        feature = []

        for _ in range(n):
            feature.append(float(data[index]))
            index += 1
        label = int(float(data[index]))
        index += 1

        distance = 0
        for dimension in range(n):
            difference = target[dimension] - feature[dimension]
            distance += difference ** 2
        distances.append((i, distance, label))

    distances.sort(key = lambda item : item[1])

    neatest = []
    neatest = distances[:k]

    label_count = {}
    for i1, d, l in neatest:
        label_count[l] = label_count.get(l, 0) + 1

    answer_count = max(label_count.values())

    answer_label = None
    for i1, d, l in neatest:
        if label_count[l] == answer_count:
            answer_label = l
            break

    print(answer_label, answer_count)


        
            



    

    # print(k, m, n, s)
    # print(target)
    # print(feature)




if __name__ == "__main__":
    main()