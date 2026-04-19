n = int(input())
s = []

for _ in range(n):
    q = input().split()
    t = int(q[0])
    
    if t == 1:
        s.append(int(q[1]))
    elif t == 2:
        if len(s) == 0:
            print('ERR_CANNOT_POP')
        else:
            s = s[1:]
    elif t == 3:
        if len(s) == 0:
            print('ERR_CANNOT_QUERY')
        else:
            print(s[0])
    elif t == 4:
        print(len(s))