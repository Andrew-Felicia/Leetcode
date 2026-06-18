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
    private void inorderTraversalRec(TreeNode root, List<Integer> result) {
        if(root == null) {
            return;
        } else {
            inorderTraversalRec(root.left, result);
            result.add(root.val);
            inorderTraversalRec(root.right, result);
        }
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        inorderTraversalRec(root, result);
        return result;
    }
}