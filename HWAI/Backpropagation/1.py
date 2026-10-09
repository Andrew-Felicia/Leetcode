import sys

#convert list to matrix
def reshape(values, rows, colums):
    return [values[row * colums:(row + 1) * colums] for row in range(rows) ]

#convert matrix to list
def flatten(matrix):
    return [
        value
        for row in matrix
        for value in row
    ]



def matmul(matrix_a, matrix_b):
    rows = len(matrix_a)
    common_dimension = len(matrix_b)
    columns = len(matrix_b[0])

    result = [
        [0.0] * columns
        for _ in range(rows)
    ]

    for row in range(rows):
        for column in range(columns):
            for common in range(common_dimension):
                result[row][column] += (
                    matrix_a[row][common]
                    * matrix_b[common][column]
                )

    return result

def transpose(matrix):
    return [
        list(column)
        for column in zip(*matrix)
    ]



def format_line(values):
    formatted = []

    for value in values:
        # Avoid printing tiny negative values as -0.00.
        if abs(value) < 0.0005:
            value = 0.0

        formatted.append(f"{value:.2f}")

    return ",".join(formatted)





def main():
    data = sys.stdin.buffer.read().decode()
    tokens = data.replace(",", " ").split()

    if not tokens:
        return
    
    index = 0
    L = int(tokens[index])
    D = int(tokens[index + 1])
    K = int(tokens[index + 2])
    learning_rate = float(tokens[index + 3])
    index += 4

    target = list(map(float,tokens[index:index + K]))
    index += K

    input_data = list(map(float, tokens[index:index + L * D]))
    index += L * D

    W_mlp_data = list(map(float, tokens[index: index + D * D]))
    index += D * D

    W_cls_data = list(map(float, tokens[index:index + D * K]))
    index += D * K


    X = reshape(input_data, L, D)
    W_mlp = reshape(W_mlp_data, D, D)
    W_cls = reshape(W_cls_data, D, K)

    ##############---forward propagation-----############

    hidden = matmul(X, W_mlp)

    scores = matmul(hidden, W_cls)



    prediction = []
    for category in range(K):
        total = 0.0
        for position in range(L):
            total += scores[position][category]
        prediction.append(total / L)


    loss = 0.0
    for category in range(K):
        difference = prediction[category] - target[category]
        loss += difference * difference

    loss /= K

    ####################################################


    ###########----back propagation-------##############

    grad_prediction = []
    for category in range(K):
        grad_prediction.append(2.0 / K * (prediction[category] - target[category]))

    grad_scores = [
        [grad_prediction[category] / L for category in range(K)]
        for _ in range(L)
    ]

    # grad_W_cls = hiddenᵀ × grad_scores
    grad_w_cls = matmul(
        transpose(hidden),
        grad_scores
    )

    # grad_hidden = grad_scores × W_clsᵀ
    # This uses the original W_cls.
    grad_hidden = matmul(
        grad_scores,
        transpose(W_cls)
    )

    # grad_W_mlp = Xᵀ × grad_hidden
    grad_w_mlp = matmul(
        transpose(X),
        grad_hidden
    )
    ####################################################

    ###########----SGD update-------####################
    new_w_mlp = [
        [
            W_mlp[i][j]
            - learning_rate * grad_w_mlp[i][j]
            for j in range(D)
        ]
        for i in range(D)
    ]

    new_w_cls = [
        [
            W_cls[j][category]
            - learning_rate * grad_w_cls[j][category]
            for category in range(K)
        ]
        for j in range(D)
    ]



    print(format_line(prediction))
    print(format_line([loss]))
    print(format_line(flatten(new_w_mlp)))
    print(format_line(flatten(new_w_cls)))





if __name__ == "__main__":
    main()