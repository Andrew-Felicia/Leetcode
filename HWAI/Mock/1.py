import sys

def main():
    n, m, h = map(int, sys.stdin.buffer.readline().split())

    colum_sum = 0
    for c in range(1, h + 1):
        colum_sum += min(c, m)

    print(colum_sum * n)





if __name__ == "__main__":
    main()