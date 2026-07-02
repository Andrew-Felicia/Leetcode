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
    private int pathSumRec(TreeNode root, int targetSum, 
                           Long currentSum, Map<Long, Integer> recorder) {
        if(root == null) {
            return 0;
        }
        currentSum += root.val;
        int count = recorder.getOrDefault(currentSum - targetSum, 0);
        
        recorder.merge(currentSum, 1, Integer::sum);

        count += pathSumRec(root.left, targetSum, currentSum, recorder);
        count += pathSumRec(root.right, targetSum, currentSum, recorder);

        recorder.merge(currentSum, -1, Integer::sum);
        

        return count;
    }
    public int pathSum(TreeNode root, int targetSum) {
        Map<Long, Integer> recorder = new HashMap<>();
        recorder.put(0L, 1);
        return pathSumRec(root, targetSum, 0L, recorder);
    }
}