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
    private int root_index = 0;

    private TreeNode buildTreeRec(int left, int right, Map<Integer, Integer> inorder_map, int[] preorder) {
            if(left > right) {
                return null;
            } 
            int root_val = preorder[root_index];
            TreeNode root = new TreeNode(root_val);
            root_index += 1;

            root.left = buildTreeRec(left, inorder_map.get(root_val) - 1, inorder_map, preorder);
            root.right = buildTreeRec(inorder_map.get(root_val) + 1, right, inorder_map, preorder);
            
            return root;
        }

    
    public TreeNode buildTree(int[] preorder, int[] inorder) {

        Map<Integer, Integer> inorder_map = new HashMap<>();
        for(int i = 0; i < inorder.length; i++) {
            inorder_map.put(inorder[i], i);
        }
        return buildTreeRec(0, inorder.length - 1, inorder_map, preorder);
    }
}