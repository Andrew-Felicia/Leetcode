# # 22. ID3 决策树训练：解答与详解

# ## 一、思路

# **1. 熵与信息增益**

# - 熵衡量一堆样本的"混乱程度"。设标签为 1 的比例是 q，则 `H = -q·log2(q) - (1-q)·log2(1-q)`。全是 0 或全是 1 时熵为 0（最纯），一半一半时熵为 1（最乱）。
# - 信息增益 = 划分前的熵 - 划分后两侧熵的加权平均。增益越大，说明这个特征把样本分得越"干净"。

# **2. 每个节点的处理流程**

# 1. 标签全相同，返回该标签（叶子）。
# 2. 在**这条路径上还没用过**的特征里，算每个特征的信息增益，选最大的。增益相同取下标小的。
# 3. 如果没有特征可用，或最大增益不大于 0，返回多数标签（平票返回 0）。
# 4. 否则按该特征值 0/1 把样本分成左、右两部分，递归建树。若某一侧为空，该侧直接作为多数标签叶子。

# **3. 预测**：从根出发，特征值为 0 走左，为 1 走右，直到叶子。

# **浮点数的坑**：增益是浮点数，"并列"的判断不能用 `==`。代码里用 `1e-12` 的误差范围：只有比当前最优大出 1e-12 才算更优，这样并列时自然保留下标小的。

# ## 二、参考代码（Python）

# ```python
import sys, math

def entropy(pos, total):
    if total == 0 or pos == 0 or pos == total:
        return 0.0
    q = pos / total
    return -(q * math.log2(q) + (1 - q) * math.log2(1 - q))

def majority(idx, y):
    pos = sum(y[i] for i in idx)
    return 1 if pos * 2 > len(idx) else 0   # 平票返回 0

def build(idx, used, X, y, m):
    total = len(idx)
    pos = sum(y[i] for i in idx)
    if pos == 0 or pos == total:
        return 1 if pos == total else 0      # 标签全同

    base = entropy(pos, total)
    best_gain, best_f = 0.0, -1
    for f in range(m):
        if used[f]:
            continue
        n1 = p1 = 0                          # 特征值为1的样本数 / 其中标签为1的数量
        for i in idx:
            if X[i][f] == 1:
                n1 += 1
                p1 += y[i]
        n0, p0 = total - n1, pos - p1
        cond = (n0 * entropy(p0, n0) + n1 * entropy(p1, n1)) / total
        gain = base - cond
        if gain > best_gain + 1e-12:         # 严格更大才替换，并列保留下标小的
            best_gain, best_f = gain, f

    if best_f == -1:                          # 没有正增益 或 特征用尽
        return majority(idx, y)

    left = [i for i in idx if X[i][best_f] == 0]
    right = [i for i in idx if X[i][best_f] == 1]
    maj = majority(idx, y)
    used[best_f] = True
    l = build(left, used, X, y, m) if left else maj
    r = build(right, used, X, y, m) if right else maj
    used[best_f] = False                      # 回溯：其他分支仍可用该特征
    return (best_f, l, r)

def predict(node, x):
    while isinstance(node, tuple):
        f, l, r = node
        node = l if x[f] == 0 else r
    return node

def main():
    data = sys.stdin.read().split()
    pos = 0
    n, m = int(data[0]), int(data[1]); pos = 2
    X, y = [], []
    for _ in range(n):
        row = list(map(int, data[pos:pos + m + 1])); pos += m + 1
        X.append(row[:m]); y.append(row[m])
    q = int(data[pos]); pos += 1

    sys.setrecursionlimit(10000)
    root = build(list(range(n)), [False] * m, X, y, m)

    out = []
    for _ in range(q):
        x = list(map(int, data[pos:pos + m])); pos += m
        out.append(str(predict(root, x)))
    print("\n".join(out))

main()
# ```

# ## 三、几个关键点

# - **`used` 要回溯**：特征"已使用"只针对**当前这条路径**。左分支用过的特征，右分支仍然可以用，所以递归返回后要把 `used[best_f]` 改回 `False`。
# - **增益 > 0 才划分**：如果所有特征增益都是 0（比如样本重复、特征无区分力），就返回多数标签。
# - **空侧情况**：只要增益为正，两侧一定都非空，所以那段保护代码实际上走不到，但按题意保留。
# - **多数标签**：`pos*2 > total` 才取 1，平票自然取 0。

# ## 四、样例手算验证

# 6 条样本中标签 3 个 0、3 个 1，根节点熵为 1。

# - 特征 1（下标 0）：值为 0 的三条标签全是 0，值为 1 的三条标签全是 1，两侧熵都为 0，**增益 = 1**。
# - 特征 2（下标 1）：每侧各 3 条，标签一侧是 1:2，另一侧是 2:1，每侧熵约 0.918，**增益 ≈ 0.082**。

# 所以选特征 1，左子树全是 0，右子树全是 1。查询 `(0,1)→0`，`(1,0)→1`，`(1,1)→1`，与样例输出一致。

# **一个小提醒**：题目的例子说明里说特征 1 与特征 2"并列"，但按计算两者增益并不相等（1 对 0.082）。结论不受影响，应该是出题说明写得不严谨。

# ## 五、复杂度

# 每个节点要对剩余特征各扫一遍样本，整体大约是 `O(n·m·深度)`，深度最多为 m。题目没给 n、m 的范围，如果规模很大（比如 n 到十万级），Python 可能偏慢，可以改写成 C++，我可以帮你改。

# 这份代码我没有实际运行，只按样例手算核对过逻辑，提交前建议本地跑一下。你也可以参考上一题的方法，用 pytest 对它做时间和内存测试。