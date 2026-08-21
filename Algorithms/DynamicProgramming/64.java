import java.util.Arrays;
class Solution {
    public int minPathSum(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        int[][] dp = new int[row + 1][col + 1];
        for (int[] tmp : dp) {
            Arrays.fill(tmp, Integer.MAX_VALUE);
        }

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (r == 0 && c == 0) {
                    dp[1][1] = grid[0][0];
                } else {
                    dp[r + 1][c + 1] = Math.min(dp[r][c + 1], dp[r + 1][c]) + grid[r][c];
                }
            }
        }

        return dp[row][col];
    }

}