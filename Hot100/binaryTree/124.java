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
class Solution {
    private int result = Integer.MIN_VALUE;
    
    private int maxPathSumRec(TreeNode root) {
        if(root == null) {
            return 0;
        } 
        int left = Math.max(0, maxPathSumRec(root.left));
        int right = Math.max(0, maxPathSumRec(root.right));

        result = Math.max(result, root.val + left + right);

        return root.val + Math.max(left, right);

    }
    public int maxPathSum(TreeNode root) {
        maxPathSumRec(root);
        return result;
    }
}