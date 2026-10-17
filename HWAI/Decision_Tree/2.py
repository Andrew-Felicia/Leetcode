import sys


def main():
    input = sys.stdin.buffer.readline
    node_count, sample_count, feature_count = map(int, input().split())

    # (left child, right child, feature index, threshold, label if pruned)
    tree = [None] * (node_count + 1)
    for node_id in range(1, node_count + 1):
        tree[node_id] = tuple(map(int, input().split()))

    samples = []
    for _ in range(sample_count):
        row = list(map(int, input().split()))
        samples.append((row[:feature_count], row[feature_count]))

    # For every node, collect the validation labels that reach it before
    # pruning. Those are exactly the samples affected if we prune that node.
    labels_at = [[] for _ in range(node_count + 1)]
    for features, true_label in samples:
        node = 1
        while True:
            labels_at[node].append(true_label)
            left, right, feature, threshold, _ = tree[node]
            if left == 0:
                break
            node = left if features[feature - 1] <= threshold else right

    infinity = sample_count + 1

    def build_dp(node):
        """
        dp[tp] = smallest FP count achievable in this subtree while getting
        exactly tp true positives.  FN is determined by the total positives.
        """
        left, right, _, _, label = tree[node]
        labels = labels_at[node]
        positive_count = sum(labels)
        negative_count = len(labels) - positive_count

        # Choice 1: prune this whole subtree and use this node's label.
        dp = [infinity] * (positive_count + 1)
        if label == 1:
            dp[positive_count] = negative_count
        else:
            dp[0] = 0

        # Leaf nodes cannot keep child subtrees.
        if left == 0:
            return dp

        # Choice 2: retain this split; left/right pruning choices combine.
        left_dp = build_dp(left)
        right_dp = build_dp(right)
        kept_dp = [infinity] * (positive_count + 1)

        for left_tp, left_fp in enumerate(left_dp):
            if left_fp == infinity:
                continue
            for right_tp, right_fp in enumerate(right_dp):
                if right_fp == infinity:
                    continue
                tp = left_tp + right_tp
                kept_dp[tp] = min(kept_dp[tp], left_fp + right_fp)

        for tp, fp in enumerate(kept_dp):
            dp[tp] = min(dp[tp], fp)

        return dp

    root_dp = build_dp(1)
    total_positive = sum(label for _, label in samples)
    best_f1 = 0.0

    for true_positive, false_positive in enumerate(root_dp):
        if false_positive == infinity:
            continue

        # F1 = 2TP / (2TP + FP + FN), FN = total_positive - TP.
        denominator = total_positive + true_positive + false_positive
        if denominator != 0:
            best_f1 = max(best_f1, 2 * true_positive / denominator)

    print(f"{best_f1:.6f}")


if __name__ == "__main__":
    main()
