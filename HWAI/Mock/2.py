import sys

def main():
    data = sys.stdin.readline
    n, m, p, k = list(map(int, data().split()))
    possibility = list(map(float, data().split()))

    if p > m:
        print("error")
        return
    if n % m != 0:
        print("error")
        return

    #grouping
    sep = n // m
    experts = [[] for _ in range(m)]
    for i, v in enumerate(possibility):
        experts[i // sep].append((v, i))
    #print(experts)

    experts_sorted = sorted(experts, key = lambda i : max(i), reverse = True)
    #print(experts_sorted)

    #picking p groups
    experts_p = experts_sorted[:p]
    #print(experts_p)

    #picking k experts
    experts_k = []
    for i in experts_p:
        for j in i:
            experts_k.append(j)
    
    result = sorted(experts_k, key = lambda i : i[0], reverse = True)
    if k > len(result):
        print("error")
        return
    
    result = result[:k]
    answer = []
    for i in result:
        answer.append(i[1])
    answer.sort()
    print(*answer)


    



if __name__ == "__main__":
    main()