/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

//If root = [2147483647], it will fail.
// class Solution {
//     private boolean isValidBSTRec(TreeNode root, int low, int high) {
//         if(root == null) {
//             return true;
//         } else if(root.val <= low || root.val >= high) {
//             return false;
//         } else {
//             return isValidBSTRec(root.left, low, root.val) && 
//             isValidBSTRec(root.right, root.val, high);
//         }
//     }
//     public boolean isValidBST(TreeNode root) {
//         return isValidBSTRec(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
//     }
// }


//use long
// class Solution {
//     private boolean isValidBSTRec(TreeNode root, long low, long high) {
//         if(root == null) {
//             return true;
//         } else if(root.val <= low || root.val >= high) {
//             return false;
//         } else {
//             return isValidBSTRec(root.left, low, root.val) && 
//             isValidBSTRec(root.right, root.val, high);
//         }
//     }
//     public boolean isValidBST(TreeNode root) {
//         return isValidBSTRec(root, Long.MIN_VALUE, Long.MAX_VALUE);
//     }
// }


//use Integer.
class Solution {
    private boolean isValidBSTRec(TreeNode root, Integer low, Integer high) {
        if (root == null) {
            return true;
        }
        
        // If low is not null, root.val must be strictly greater than low
        if (low != null && root.val <= low) return false;
        // If high is not null, root.val must be strictly less than high
        if (high != null && root.val >= high) return false;
        
        return isValidBSTRec(root.left, low, root.val) && 
               isValidBSTRec(root.right, root.val, high);
    }
    
    public boolean isValidBST(TreeNode root) {
        // null means there are no boundary restrictions yet
        return isValidBSTRec(root, null, null);
    }
}