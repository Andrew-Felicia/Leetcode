import math
import sys


LEARNING_RATE = 0.1
EPOCHS = 20


def encode(text):
    """Return the A-G presence vector for one feature sequence."""
    present = set(text)
    return [1.0 if letter in present else 0.0 for letter in "ABCDEFG"]


def sigmoid(value):
    # This form avoids overflow if value is a large negative number.
    if value >= 0:
        return 1.0 / (1.0 + math.exp(-value))

    exp_value = math.exp(value)
    return exp_value / (1.0 + exp_value)


def main():
    input = sys.stdin.buffer.readline
    training_count, test_count = map(int, input().split())

    training_data = []
    for _ in range(training_count):
        text, label = input().split()
        training_data.append((encode(text.decode()), int(label)))

    test_data = [input().strip().decode() for _ in range(test_count)]

    # Seven weights correspond to A, B, C, D, E, F, G.
    weights = [0.0] * 7
    bias = 0.0

    # Batch size = 1: update immediately after each training sample.
    for _ in range(EPOCHS):
        for features, true_label in training_data:
            z = sum(weight * feature for weight, feature in zip(weights, features)) + bias
            prediction = sigmoid(z)

            # For sigmoid + binary cross-entropy, d(loss)/d(z) is p - y.
            error = prediction - true_label

            for index in range(7):
                weights[index] -= LEARNING_RATE * error * features[index]

            bias -= LEARNING_RATE * error

    for text in test_data:
        features = encode(text)
        z = sum(weight * feature for weight, feature in zip(weights, features)) + bias
        prediction = sigmoid(z)

        # The problem says strictly greater than 0.5 means label 1.
        print(1 if prediction > 0.5 else 0)


if __name__ == "__main__":
    main()
