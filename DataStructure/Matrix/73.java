class Solution {
    public void setZeroes(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;

        Set<int[]> recorder = new HashSet<>();
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                if(matrix[i][j] == 0) {
                    int[] tmp = new int[2];
                    tmp[0] = i;
                    tmp[1] = j;
                    recorder.add(tmp);
                }
                
            }
        }

        for(int[] i : recorder) {
            for(int x = 0; x < row; x++) {
                matrix[x][i[1]] = 0;

            }

            for(int y = 0; y < col; y++) {
                matrix[i[0]][y] = 0;
            }
        }
    }
}