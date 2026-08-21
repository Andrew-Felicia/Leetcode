import sys


def placement_counts(s):
    n = len(s)
    frequency = [0] * (n + 1)
    run = 0
    for character in s + "b":
        if character == "a":
            run += 1
        elif run:
            frequency[run] += 1
            run = 0

    count = [0] * (n + 1)
    runs = 0
    lengths = 0
    for size in range(n, 0, -1):
        runs += frequency[size]
        lengths += frequency[size] * size
        count[size] = lengths - (size - 1) * runs
    return count


def count_rectangles(a, b, area):
    rows, columns = placement_counts(a), placement_counts(b)
    answer = 0
    divisor = 1
    while divisor * divisor <= area:
        if area % divisor == 0:
            other = area // divisor
            if divisor < len(rows) and other < len(columns):
                answer += rows[divisor] * columns[other]
            if divisor != other and other < len(rows) and divisor < len(columns):
                answer += rows[other] * columns[divisor]
        divisor += 1
    return answer


def main():
    tokens = sys.stdin.buffer.read().split()
    n, m, area = map(int, tokens[:3])
    print(count_rectangles(tokens[3].decode()[:n], tokens[4].decode()[:m], area))


if __name__ == "__main__":
    main()
