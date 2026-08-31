import sys


def construct_smallest(counts):
    counts = list(counts)
    remaining = sum(counts)

    if remaining and max(counts) > (remaining + 1) // 2:
        return None

    answer = []
    previous = -1

    while remaining:
        suffix_length = remaining - 1
        same_limit = suffix_length // 2
        other_limit = (suffix_length + 1) // 2
        chosen = -1

        for rating in range(5):
            if rating == previous or counts[rating] == 0:
                continue

            counts[rating] -= 1
            feasible = counts[rating] <= same_limit

            if feasible:
                for other in range(5):
                    if other != rating and counts[other] > other_limit:
                        feasible = False
                        break

            if feasible:
                chosen = rating
                break

            counts[rating] += 1

        if chosen == -1:
            return None

        answer.append(str(chosen + 1))
        previous = chosen
        remaining -= 1

    return answer


def solve(data):
    tokens = iter(data.split())
    n = int(next(tokens))
    counts = [0] * 5

    for _ in range(n):
        counts[int(next(tokens)) - 1] += 1

    answer = construct_smallest(counts)
    return "-1" if answer is None else " ".join(answer)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))