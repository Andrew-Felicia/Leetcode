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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root == null) {
            return new ArrayList<>();
        } else if(root.left == null && root.right == null) {
            List<Integer> tmp = new ArrayList<>();
            List<List<Integer>> tmp1 = new ArrayList<>();
            tmp.add(root.val);
            tmp1.add(tmp);
            return tmp1; 
        } else {
            List<List<Integer>> left = levelOrder(root.left);
            List<List<Integer>> right = levelOrder(root.right);
            List<List<Integer>> result = new ArrayList<>();

            int size = Math.max(left.size(), right.size());
            for(int i = 0; i < size; i++) {
                List<Integer> combine = new ArrayList<>();
                if(i < left.size()) {
                    combine.addAll(left.get(i));
                }
                if(i < right.size()) {
                    combine.addAll(right.get(i));
                }
                result.add(combine);
            }

            List<Integer> rootlevel = new ArrayList<>();
            rootlevel.add(root.val);
            result.add(0, rootlevel);
            return result;

        }
    }
}