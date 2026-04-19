n = int(input())
s = []

for _ in range(n):
    p = input().split()
    if p[0] == 'push':
        s.append(int(p[1]))
    elif p[0] == 'pop':
        if len(s) == 0:
            print('Empty')
        else:
            s.pop()
    elif p[0] == 'query':
        if len(s) == 0:
            print('Empty')
        else:
            print(s[-1])
    elif p[0] == 'size':
        print(len(s))