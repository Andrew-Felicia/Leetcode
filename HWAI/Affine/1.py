import math
import sys


def nearest_integer(value):
    """Round a coordinate to its nearest integer; .5 rounds upward."""
    return math.floor(value + 0.5)


def main():
    input = sys.stdin.buffer.readline

    image_height, matrix_rows, _ = map(int, input().split())

    image = [
        list(map(int, input().split()))
        for _ in range(image_height)
    ]

    matrix = [
        list(map(float, input().split()))
        for _ in range(matrix_rows)
    ]

    output_height, output_width = map(int, input().split())

    a, b, tx = matrix[0]
    c, d, ty = matrix[1]

    determinant = a * d - b * c

    # A singular linear transformation has no inverse.
    if abs(determinant) < 1e-12:
        print(*([0] * (output_height * output_width)))
        return

    source_height = len(image)
    source_width = len(image[0])
    output = []

    # Visit every position in the output image and map it backward
    # to the corresponding position in the source image.
    for output_y in range(output_height):
        for output_x in range(output_width):
            shifted_x = output_x - tx
            shifted_y = output_y - ty

            source_x = (
                d * shifted_x - b * shifted_y
            ) / determinant
            source_y = (
                -c * shifted_x + a * shifted_y
            ) / determinant

            source_x = nearest_integer(source_x)
            source_y = nearest_integer(source_y)

            if (
                0 <= source_x < source_width
                and 0 <= source_y < source_height
            ):
                output.append(image[source_y][source_x])
            else:
                output.append(0)

    print(*output)


if __name__ == "__main__":
    main()
