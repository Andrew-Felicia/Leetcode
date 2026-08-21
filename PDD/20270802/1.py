import sys

#brute force
#O(n^3)
# def main():

#     data = sys.stdin.read().split()
#     idx = 0
#     n = int(data[idx])
#     idx += 1
#     s = data[idx]

#     def abEqual(start, end):
#         a, b = 0, 0
#         for i in s[start:end + 1]:
#             if i == 'A':
#                 a += 1
#             else:
#                 b += 1
#         return a == b
    
#     best = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if abEqual(i, j):
#                 best = max(best, j - i + 1)
#     print(best)



#hash table + prefix sum
def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    s = data[idx]

    best = 0
    balance = 0
    prefix = {0:-1}
    for i, c in enumerate(s):
        if c == 'A':
            balance += 1
        else:
            balance -= 1
        if balance in prefix:
            best = max(best, i - prefix[balance])
        else:
            prefix[balance] = i
    print(best)






if __name__ == "__main__":
    main()