import math
import sys


def sigmoid(z):
    z = max(-500.0, min(500.0, z))
    return 1.0 / (1.0 + math.exp(-z))


def compute_loss(X, y, w, b, lam):
    n = len(X)
    eps = 1e-12
    total = 0.0
    for xi, yi in zip(X, y):
        p = sigmoid(sum(wj * xj for wj, xj in zip(w, xi)) + b)
        total += -(yi * math.log(p + eps) + (1 - yi) * math.log(1 - p + eps))
    return total / n + lam / (2 * n) * sum(wj * wj for wj in w)


def train(X, y, max_iter, lr, lam, tol):
    n = len(X)
    d = len(X[0])
    w = [0.0] * d
    b = 0.0
    prev = compute_loss(X, y, w, b, lam)
    for _ in range(max_iter):
        grad_w = [0.0] * d
        grad_b = 0.0
        for xi, yi in zip(X, y):
            err = sigmoid(sum(wj * xj for wj, xj in zip(w, xi)) + b) - yi
            for j in range(d):
                grad_w[j] += err * xi[j]
            grad_b += err
        for j in range(d):
            w[j] -= lr * (grad_w[j] / n + lam / n * w[j])
        b -= lr * (grad_b / n)
        cur = compute_loss(X, y, w, b, lam)
        if abs(prev - cur) < tol:
            break
        prev = cur
    return w, b


def main():
    tokens = sys.stdin.read().split()
    pos = 0
    n = int(float(tokens[pos])); pos += 1
    max_iter = int(float(tokens[pos])); pos += 1
    lr = float(tokens[pos]); pos += 1
    lam = float(tokens[pos]); pos += 1
    tol = float(tokens[pos]); pos += 1

    X, y = [], []
    for _ in range(n):
        row = [float(t) for t in tokens[pos:pos + 4]]
        pos += 4
        X.append(row[:3])
        y.append(row[3])

    m = int(float(tokens[pos])); pos += 1
    tests = []
    for _ in range(m):
        tests.append([float(t) for t in tokens[pos:pos + 3]])
        pos += 3

    w, b = train(X, y, max_iter, lr, lam, tol)

    out = []
    for xi in tests:
        p = sigmoid(sum(wj * xj for wj, xj in zip(w, xi)) + b)
        out.append(f"{1 if p >= 0.5 else 0} {p:.4f}")
    print("\n".join(out))


if __name__ == "__main__":
    main()