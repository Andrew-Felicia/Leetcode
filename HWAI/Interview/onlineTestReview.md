
## 1.
```python
def solve(t, s, k):
    n = len(t)

    # 前缀和，快速计算区间计算耗时
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + t[i]

    INF = float('inf')

    # dp[j][i]: 前 i 层划分成 j 个连续阶段的最优解
    dp = [[INF] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for j in range(1, k + 1):
        for i in range(j, n + 1):
            # 最后一个阶段为 [p, i-1]
            for p in range(j - 1, i):
                compute = prefix[i] - prefix[p]

                # 阶段结束后仍有下一层，才产生通信成本
                comm = s[i - 1] if i < n else 0
                cost = compute + comm

                dp[j][i] = min(
                    dp[j][i],
                    max(dp[j - 1][p], cost)
                )

    return dp[k][n]

```
# 示例 1
print(solve([10], [0], 1))  # 10

# 示例 2
print(solve(
    [10, 20, 15, 25, 30],
    [5, 10, 5, 20, 0],
    3
))  # 50



# input:   t： 一个长度为n的整数数组，表示每层的计算时间
# s: 一个长度为n的整数数组，表示每层输出的通信时间
# k：gpu的数量

# output:一个整数， 表示最小化的单个gpu最大总耗时

# example1：
# input:
# 10
# 0
# 1
# output:
# 10


# example2:
# input:
# 10 20 15 25 30
# 5 10 5 20 0
# 3
# output:
# 50

# 用python 解决

# 只通过了40%的测试， 也许是背景给的不够，我增加一下背景：
# 你正在将一个包含n个层的深度神经网络部署到k个gpu上，采用流水线并行的策略

# 已知每一层的计算耗时为t[i]
# 每一层的输出张量大小为s[i].
# 通信成本：如果i层和i+1层被分配在不同gpu上会产生s[i]的通信耗时,如果在相同gpu上则通信耗时为0，
# 你需要将这个n层模型切分为k个阶段，每个阶段分配给一个gpu,使得单个gpu的最大总耗时（计算耗时+通信耗时）最小

# 注意：由于是流水线，你必须将模型切分为k个连续的子序列



## 2. 

decision tree
