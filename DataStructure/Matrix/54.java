class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int row = matrix.length;
        int col = matrix[0].length;

        int left = 0;
        int right = col - 1;
        int top = 0;
        int bottom = row - 1;

        while(left <= right && top <= bottom) {
            for(int col_variable = left; col_variable <= right; col_variable++) {
                result.add(matrix[top][col_variable]);
            }
            for(int row_variable = top + 1; row_variable <= bottom; row_variable++) {
                result.add(matrix[row_variable][right]);
            }
            if(left < right && top < bottom) { //why we need this if statement?
                for(int col_variable = right - 1; col_variable >= left ; col_variable--) {
                    result.add(matrix[bottom][col_variable]);
                }
                for(int row_variable = bottom - 1; row_variable > top; row_variable--) {
                    result.add(matrix[row_variable][left]);
                }
            }
            

            left += 1;
            right -= 1;
            top += 1;
            bottom -= 1;
        }

        return result;
    }
}