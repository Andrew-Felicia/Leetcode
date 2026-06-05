import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[][] matrix = { {1, 4}, {2, 5} };
        System.out.println(searchMatrix(matrix, 2));
          //way 2
//        int[][] matrix; // Declaration
//
//       // Later in your code...
//        matrix = new int[][] { {1, 4}, {2, 5} }; // Explicit Initialization

    }

    private static boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        int col = matrix[0].length;

        int left = 0;
        int right = row * col - 1;

        while(left <= right) {
            int mid = (left + right) / 2;

            int value = matrix[mid / col][mid % col];

            if(value == target) return true;

            if(value > target) {
                right = mid - 1;
            }

            if(value < target) {
                left = mid + 1;
            }
        }
        return false;
    }
}

