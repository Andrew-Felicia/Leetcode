class Solution:
    def minDistance(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        #dfs(i, j) returns the minimum edit distance between
        #s[0:i] and t[0:j]
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if s[i] == t[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1
        return dfs(n - 1, m - 1)