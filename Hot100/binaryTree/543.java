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
    int maxDiameter = 0;
    //this function return the height of a tree.
    private int heightOfTree(TreeNode root) {
        if(root == null) return 0;

        int left = heightOfTree(root.left);
        int right = heightOfTree(root.right);
        //the diameter at this node is it's left subtree height plus it's right subtree height.
        maxDiameter = Math.max(maxDiameter, left + right);

        return 1 + Math.max(left, right);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        heightOfTree(root);
        return maxDiameter;
    }
}