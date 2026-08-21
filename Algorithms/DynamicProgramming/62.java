//recursive + memo
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] memo = new int[m][n];
        return dfs(m - 1, n - 1, memo);

    }

    private int dfs(int m, int n, int[][] memo) {
        if (m < 0 || n < 0) {
            return 0;
        }

        if (m == 0 && n == 0) {
            return 1;
        }

        if (memo[m][n] != 0) {
            return memo[m][n];        
        }

        memo[m][n] = dfs(m - 1, n, memo) + dfs(m, n - 1, memo);
        return memo[m][n];
    }
}


//dynamic programming.
import java.util.Arrays;

class Solution {
    public int uniquePaths(int m, int n) {
        int[][] path = new int[m + 1][n + 1];
        for (int[] row : path) {
            Arrays.fill(row, 0);
        }

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (r == 0 && c == 0) {
                    path[1][1] = 1;
                } else {
                    path[r + 1][c + 1] = path[r][c + 1] + path[r + 1][c];
                }
            }
        }

        return path[m][n];
    }
}