class Solution {
    private int r = 0;
    private int c = 0;
    private void dfs(char[][] grid, int r, int c) {
        if(r < 0 || r >= this.r || c < 0 || c >= this.c || grid[r][c] == '0') {
            return;
        }
        grid[r][c] = '0';
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
    public int numIslands(char[][] grid) {
        this.r = grid.length;
        this.c = grid[0].length;
        int result = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if(grid[i][j] == '1') {
                    dfs(grid, i, j);
                    result += 1;
                }
            }
        }
        return result;
    }
}