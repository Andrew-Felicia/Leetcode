import sys

MOD = 998244353


def count_pairs(values, modulus):
    counts = [0] * modulus
    answer = 0
    for value in values:
        remainder = value % modulus
        answer += counts[-remainder % modulus]
        counts[remainder] += 1
    return answer % MOD


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n, modulus = numbers[0], numbers[1]
    print(count_pairs(numbers[2:2+n], modulus))


if __name__ == "__main__":
    main()
