class Solution {
    private static final int[][] DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int orangesRotting(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int fresh_count = 0;
        List<int[]> queue = new ArrayList<>();

        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                if(grid[i][j] == 1) {
                    fresh_count += 1;
                } else if(grid[i][j] == 2) {
                    queue.add(new int[]{i, j});
                }
            }
        }
        if(fresh_count == 0) return 0;

        int minutes = 0;
        while(!queue.isEmpty() && fresh_count > 0) {
            List<int[]> tmp = queue;
            queue = new ArrayList<>();
            minutes += 1;
            for(int[] pos : tmp) {
                for(int[] dir : DIRECTIONS) {
                    int pos_r = pos[0] + dir[0];
                    int pos_c = pos[1] + dir[1];
                    if(pos_r >= 0 && pos_r < row && pos_c >=0 && pos_c < col &&
                       grid[pos_r][pos_c] == 1) {
                        grid[pos_r][pos_c] = 2;
                        fresh_count -= 1;
                        queue.add(new int[]{pos_r, pos_c});
                    }
                }
            }
        }

        return (fresh_count == 0) ? minutes : -1;
    }
}