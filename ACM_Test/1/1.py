n = int(input())

s = []
for _ in range(n):
    q = input().split()
    m = int(q[0])

    if m == 1:
        s.append(int(q[1]))
    if m == 2:
        s.pop()
    if m == 3:
        print(s[int(q[1])])
    if m == 4:
        s.insert(int(q[1]) + 1, int(q[2]))
    if m == 5:
        s.sort()
    if m == 6:
        s.sort(reverse = True)
    if m == 7:
        print(len(s))
    if m == 8:
        print(*s)

