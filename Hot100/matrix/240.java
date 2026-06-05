//flaw
// class Solution {
//     public boolean searchMatrix(int[][] matrix, int target) {
//         int row = matrix.length;
//         int col = matrix[0].length;

//         int left = 0;
//         int right = row * col - 1;

//         while(left <= right) {
//             int mid = (left + right) / 2;

//             int value = matrix[mid / col][mid % col];

//             if(value == target) return true;

//             if(value > target) {
//                 right = mid - 1;
//             }

//             if(value < target) {
//                 left = mid + 1;
//             }
//         }
//         return false;
//     }
// }

//flaw
// class Solution {
//     public boolean searchMatrix(int[][] matrix, int target) {
//         int row = matrix.length;
//         int col = matrix[0].length;
//         int i = 0;
//         int j = col - 1;

//         while(j >= 0 && i < row) {
//             if(matrix[i][j] == target) return true;

//             if(matrix[i][j] > target) {
//                 j -= 1;
//             }

//             if(matrix[i][j] < target) {
//                 i += 1;
//             }
//         }

//         return false;
//     }
// }


class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        int col = matrix[0].length;
        int i = 0;
        int j = col - 1;

        while(j >= 0 && i < row) {
            if(matrix[i][j] == target) {
                return true;
            } else if(matrix[i][j] > target) {
                j -= 1;
            } else {
                i += 1;
            }
        }

        return false;
    }
}