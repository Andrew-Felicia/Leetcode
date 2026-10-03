#knapsack, dynamic programming.
import sys

def main():
    input = sys.stdin.buffer.readline
    first_line = input().split()
    L = int(first_line[0])
    T = float(first_line[1])

    data = []
    for _ in range(L):
        parts = input().split()
        K = int(parts[0])

        layer = []
        index = 1
        for i in range(K):
            #bit_wides = parts[index].decode()
            loss = float(parts[index + 1])
            memory = float(parts[index + 2])
            layer.append([loss, memory])
            index += 3
        data.append(layer)
    #print(data)

    # Convert floating-point loss into an integer.
    # SCALE = 100 supports up to two decimal places.
    SCALE = 100
    max_loss = round(T * SCALE)

    INF = float("inf")

    # dp[x] = minimum memory when the total loss is exactly x
    dp = [INF] * (max_loss + 1)
    dp[0] = 0.0

    # Process one layer at a time
    for layer in data:
        new_dp = [INF] * (max_loss + 1)

        for current_loss in range(max_loss + 1):
            if dp[current_loss] == INF:
                continue

            # Select one option from the current layer
            for loss, memory in layer:
                option_loss = round(loss * SCALE)
                new_loss = current_loss + option_loss

                if new_loss <= max_loss:
                    new_dp[new_loss] = min(
                        new_dp[new_loss],
                        dp[current_loss] + memory
                    )

        dp = new_dp

    # Total loss may be smaller than T, so check all valid states.
    answer = min(dp)

    if answer == INF:
        print("-1")
    else:
        print(f"{answer:.2f}")







if __name__ == "__main__":
    main()