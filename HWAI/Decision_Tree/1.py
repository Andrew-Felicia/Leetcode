import sys

#return a list.
def predict(tree, datas):
    tree_index = 0
    while True:
        s, threshold, left, right, result = tree[tree_index]
        if result != -1:
            return result
        if datas[s] <= threshold:
            tree_index = left
        else:
            tree_index = right



def main():
    input = sys.stdin.buffer.readline
    f, m, n = map(int, input().split())
    tree = []
    for _ in range(m):
        node = input().split()
        tree.append((int(node[0]), float(node[1]), int(node[2]), int(node[3]), int(node[4])))

    datas = []
    for _ in range(n):
        datas.append(list(map(float, input().split())))

    # print(tree)
    # print(datas)

    result = []
    for data in datas:
        result.append(predict(tree, data))

    for i in result:
        print(i)

    


if __name__ == "__main__":
    main()