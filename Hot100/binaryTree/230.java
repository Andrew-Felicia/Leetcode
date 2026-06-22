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
    private int ans = 0;
    private int k = 0;

    //inorder traversal.
    private void dfs(TreeNode root) {
        if(root == null || this.k <= 0) {
            return;
        }

        dfs(root.left);
        this.k -= 1;
        if(this.k == 0) {
            this.ans = root.val;
        }
        dfs(root.right);
    }

    public int kthSmallest(TreeNode root, int k) {
        this.k = k;
        dfs(root);
        return this.ans;
    }
}