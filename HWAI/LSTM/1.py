import math
import sys


def format_number(value):
    # Round to three decimal places, then remove unnecessary trailing zeros.
    text = f"{value:.3f}".rstrip("0").rstrip(".")

    # The problem requires zero to be printed as 0.0.
    if text == "0" or text == "-0":
        return "0.0"

    return text


def main():
    data = sys.stdin.buffer.read().split()

    if not data:
        return

    seq_len = int(data[0])
    x_dim = int(data[1])

    # The following seq_len * x_dim input values are intentionally unused:
    # all weights and biases are fixed at zero in this problem.
    result = []

    for t in range(1, seq_len + 1):
        cell_state = 0.5 ** t
        hidden_value = 0.5 * math.tanh(cell_state)
        result.append(format_number(hidden_value))

    print(" ".join(result))


if __name__ == "__main__":
    main()