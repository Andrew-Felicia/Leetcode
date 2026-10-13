import sys

def main():
    i, p, c, e = list(map(int, sys.stdin.readline().split()))
    print((i // p) ** 2 + 1, e)


if __name__ == "__main__":
    main()