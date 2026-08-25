import sys




def solve(s):
    record = {0:-1}
    balance = 0
    ans = 0
    for i, v in enumerate(s):
        if v == 'A':
            balance += 1
        else:
            balance -= 1
        if balance in record:
            ans = max(ans, i - record[balance])
        else:
            record[balance] = i
    return ans




def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    print(solve(s))


if __name__ == "__main__":
    main()