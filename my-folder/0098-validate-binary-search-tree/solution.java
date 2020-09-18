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
    public boolean isValidBST(TreeNode root) {
        
        return helper(root, null, null);
    }
    
    public boolean helper(TreeNode root, Integer upper, Integer lower){
        if(root==null){
            return true;
        }
        
         if(upper!=null&&root.val>=upper||lower!=null&&root.val<=lower){
            return false;
        }
        
        return helper(root.left, root.val, lower) && helper(root.right, upper, root.val);
    }
}
