import sys



def main():
    data = sys.stdin.buffer.readline
    pred = list(map(int, data().split()))
    true = list(map(int, data().split()))
    weights = list(map(float, data().split()))

    N = len(weights)

    # print(pred)
    # print(true)
    # print(weights)

    tfpn = [[0,0,0] for _ in range(N)]   # [TP, FP, FN]
    prf1 = [[0.0,0.0,0.0] for _ in range(N)] #[precision, recall, f1]

    #O(n^2)
    for i in range(N):
        for p, t in zip(pred, true):
            if p == i and t == i:
                tfpn[i][0] += 1
            if p == i and t != i:
                tfpn[i][1] += 1
            if p != i and t == i:
                tfpn[i][2] += 1

    #print(tfpn)

    for index, item in enumerate(tfpn):
        tp, fp, fn = item
        if tp + fp != 0:
            prf1[index][0] = round(tp / (tp + fp), 2)
        if tp + fn != 0:
            prf1[index][1] = round(tp / (tp + fn), 2)
        if prf1[index][0] + prf1[index][1] != 0:
            prf1[index][2] = round((2 * prf1[index][0] * prf1[index][1]) / (prf1[index][0] + prf1[index][1]), 2)
    #print(prf1)

    precision = 0.0
    recall = 0.0
    f1score = 0.0
    for index, item in enumerate(prf1):
        p, r, f = item
        precision += p * weights[index]
        recall += r * weights[index]
        f1score += f * weights[index]

    #print(round(precision, 2), round(recall, 2), round(f1score, 2))
    #print(precision, recall, f1score)
    print(f"{precision:.2f}", f"{recall:.2f}", f"{f1score:.2f}")










if __name__ == "__main__":
    main()