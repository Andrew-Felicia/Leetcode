import sys


def calculate_energy_matrix(image, strategy):
    height = len(image)
    width = len(image[0])
    kernel_size = len(strategy)

    padding = kernel_size // 2

    energy = [
        [0.0] * width
        for _ in range(height)
    ]

    for row in range(height):
        for col in range(width):
            total = 0.0

            for kernel_row in range(kernel_size):
                for kernel_col in range(kernel_size):
                    image_row = row + kernel_row - padding
                    image_col = col + kernel_col - padding

                    if (
                        0 <= image_row < height
                        and 0 <= image_col < width
                    ):
                        total += (
                            image[image_row][image_col]
                            * strategy[kernel_row][kernel_col]
                        )

            energy[row][col] = total

    return energy


def find_path(power):
    height = len(power)
    width = len(power[0])

    dp = [[0.0] * width for _ in range(height)]

    for row in range(height):
        dp[row][0] = power[row][0]

    for col in range(1, width):
        for row in range(height):
            best_previous = dp[row][col - 1]
            if row > 0:
                best_previous = max(best_previous, dp[row - 1][col - 1])
            if row < height - 1:
                best_previous = max(best_previous, dp[row + 1][col - 1])
            dp[row][col] = best_previous + power[row][col]

    return max(dp[row][width - 1] for row in range(height))


def main():
    data = sys.stdin.readline
    h, w, k1, k2 = list(map(int, data().split()))
    image = list(list(map(float, data().split())) for _ in range(h)) 
    strategy = list(list(map(float, data().split())) for _ in range(k1))

    power = calculate_energy_matrix(image, strategy)

    answer = find_path(power)
    print(f"{answer:.1f}")


if __name__ == "__main__":
    main()