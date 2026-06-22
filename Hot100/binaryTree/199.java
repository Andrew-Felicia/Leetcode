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
    private List<Integer> result = new ArrayList<>();
    private int depth = 0;

    private void dfs(TreeNode root, int depth) {
        if(root == null) {
            return;
        }
        if(depth == this.result.size()) {
            result.add(root.val);
        }
        dfs(root.right, depth + 1);
        dfs(root.left, depth + 1);

    }
    public List<Integer> rightSideView(TreeNode root) {
        dfs(root, this.depth);
        return this.result;
    }
}