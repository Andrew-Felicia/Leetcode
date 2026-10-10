import sys
import math


def solve_linear_system(matrix, values):
    """
    Solve matrix * x = values using Gauss-Jordan elimination.
    """

    n = len(values)

    # Create the augmented matrix [matrix | values]
    augmented = [
        matrix[row][:] + [values[row]]
        for row in range(n)
    ]

    for column in range(n):
        # Partial pivoting: choose the row with the largest
        # absolute value in the current column.
        pivot_row = max(
            range(column, n),
            key=lambda row: abs(augmented[row][column])
        )

        augmented[column], augmented[pivot_row] = (
            augmented[pivot_row],
            augmented[column]
        )

        pivot = augmented[column][column]

        # The problem guarantees that an analytical solution exists.
        if abs(pivot) < 1e-12:
            raise ValueError("No unique solution")

        # Make the pivot equal to 1.
        for j in range(column, n + 1):
            augmented[column][j] /= pivot

        # Eliminate this variable from all other rows.
        for row in range(n):
            if row == column:
                continue

            factor = augmented[row][column]

            for j in range(column, n + 1):
                augmented[row][j] -= (
                    factor * augmented[column][j]
                )

    return [
        augmented[row][n]
        for row in range(n)
    ]


def round_half_up(value):
    """Perform conventional rounding instead of banker's rounding."""

    if value >= 0:
        return math.floor(value + 0.5)

    return math.ceil(value - 0.5)


def main():
    data = sys.stdin.buffer.read().split()

    if not data:
        return

    index = 0

    # Number of known phones
    K = int(data[index])
    index += 1

    # XᵀX is a 4×4 matrix because the model has:
    # bias + three feature weights.
    xtx = [
        [0.0] * 4
        for _ in range(4)
    ]

    # Xᵀy is a vector with four elements.
    xty = [0.0] * 4

    for _ in range(K):
        hardware = float(data[index])
        system = float(data[index + 1])
        ai = float(data[index + 2])
        price = float(data[index + 3])
        index += 4

        # The first 1 represents the bias term.
        features = [1.0, hardware, system, ai]

        # Calculate XᵀX and Xᵀy directly.
        for i in range(4):
            xty[i] += features[i] * price

            for j in range(4):
                xtx[i][j] += features[i] * features[j]

    # Solve for [bias, w1, w2, w3].
    weights = solve_linear_system(xtx, xty)

    N = int(data[index])
    index += 1

    answers = []

    for _ in range(N):
        hardware = float(data[index])
        system = float(data[index + 1])
        ai = float(data[index + 2])
        index += 3

        prediction = (
            weights[0]
            + weights[1] * hardware
            + weights[2] * system
            + weights[3] * ai
        )

        answers.append(str(round_half_up(prediction)))

    print(" ".join(answers))


if __name__ == "__main__":
    main()