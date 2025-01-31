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
    public TreeNode invertTree(TreeNode root) {
      // use Stack
      if (root == null) return null;
      
      Stack<TreeNode> stack = new Stack<>();
      stack.push(root);
      
      while (!stack.isEmpty()) {
        TreeNode node = stack.pop();
        TreeNode left = node.left;
        node.left = node.right;
        node.right = left; 
        
        if (node.left != null) stack.push(node.left);
        if (node.right != null) stack.push(node.right);
      }
      return root;
    }
}
