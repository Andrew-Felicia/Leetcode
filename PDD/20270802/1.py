import sys


def longest_balanced(s):
    earliest = {0: -1}
    balance = 0
    answer = 0
    for index, character in enumerate(s):
        balance += 1 if character == "A" else -1
        if balance in earliest:
            answer = max(answer, index - earliest[balance])
        else:
            earliest[balance] = index
    return answer


def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    print(longest_balanced(tokens[1].decode()[:n]))


if __name__ == "__main__":
    main()
