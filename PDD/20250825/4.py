import sys


def longest_alternating(s):
    zeroes = s.count("0")
    ones = len(s) - zeroes
    return 2 * min(zeroes, ones) + (zeroes != ones)


def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    s = tokens[1].decode()
    print(longest_alternating(s[:n]))


if __name__ == "__main__":
    main()
