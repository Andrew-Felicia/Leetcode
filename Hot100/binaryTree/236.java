/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || root == p || root == q) {
            return root;
        }
        TreeNode left_acs = lowestCommonAncestor(root.left, p, q);
        TreeNode right_acs = lowestCommonAncestor(root.right, p, q);

        if(left_acs != null && right_acs != null) {
            return root;
        }

        return (left_acs == null) ? right_acs : left_acs;
    }
}