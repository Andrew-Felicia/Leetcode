s = []

def lower_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

def insertValue(x):
    i = lower_bound(s, x)
    if i == len(s) or s[i] != x:
        s.insert(i, x)

def eraseValue(x):
    i = lower_bound(s, x)
    if i < len(s) and s[i] == x:
        s.pop(i)

def xInSet(x):
    i = lower_bound(s, x)
    if i < len(s) and s[i] == x:
        return True
    else:
        return False

def sizeOfSet():
    return len(s)

def getPre(x):
    i = lower_bound(s, x)
    if i == 0:
        return -1
    else:
        return s[i - 1]

def getBack(x):
    i = lower_bound(s, x)
    if i < len(s) and s[i] == x:
        i += 1
    if i >= len(s):
        return -1
    return s[i]


def main():
    q = int(input())
    for _ in range(q):
        line = map(int,input().split())
        cnt,op,x=0,0,0
        for i in line:
            if(cnt==0):
                op=i
            else:
                x=i
            cnt+=1
        
        if op == 1:
            insertValue(x)
        elif op == 2:
            eraseValue(x)
        elif op == 3:
            print("YES" if xInSet(x) else "NO")
        elif op == 4:
            print(sizeOfSet())
        elif op == 5:
            print(getPre(x))
        elif op == 6:
            print(getBack(x))

if __name__ == "__main__":
    main()



#################################################################################################
#another way


import bisect

M = []  # 用一个有序 list 维护集合

def insertValue(x):
    i = bisect.bisect_left(M, x)
    if i == len(M) or M[i] != x:
        M.insert(i, x)

def eraseValue(x):
    i = bisect.bisect_left(M, x)
    if i < len(M) and M[i] == x:
        M.pop(i)

def xInSet(x):
    i = bisect.bisect_left(M, x)
    return i < len(M) and M[i] == x

def sizeOfSet():
    return len(M)

def getPre(x):
    i = bisect.bisect_left(M, x)
    if i == 0:
        return -1
    return M[i - 1]

def getBack(x):
    i = bisect.bisect_right(M, x)
    if i == len(M):
        return -1
    return M[i]

def main():
    n = int(input())
    for _ in range(n):
        op = list(map(int, input().split()))

        if op[0] == 1:
            insertValue(op[1])
        elif op[0] == 2:
            eraseValue(op[1])
        elif op[0] == 3:
            print("YES" if xInSet(op[1]) else "NO")
        elif op[0] == 4:
            print(sizeOfSet())
        elif op[0] == 5:
            print(getPre(op[1]))
        elif op[0] == 6:
            print(getBack(op[1]))

if __name__ == "__main__":
    main()
