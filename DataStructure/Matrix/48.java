class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        //Transpose
        for(int i = 1; i < n; i++) {
            for(int j = 0; j < i; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;

            }
        }
        
        //reverse.
        for(int i = 0; i < n; i++) {
            int left = 0;
            int right = n - 1;
            while(left < right) {
                int tmp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = tmp;
                left++;
                right--;
            }
        }

    }
}