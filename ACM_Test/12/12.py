n = int(input())

for _ in range(n):
    tmp = input()
    s = list(map(int, input().split()))
    print(sum(s))