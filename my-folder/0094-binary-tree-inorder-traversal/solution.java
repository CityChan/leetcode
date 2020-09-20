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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        helper(stack, root);
        while(!stack.isEmpty()){
            TreeNode node = stack.pop();
            list.add(node.val);
            helper(stack, node.right);
        }
        return list;
    }
    
    private void helper(Deque<TreeNode> stack, TreeNode root){
        while(root!=null){
            stack.push(root);
            root = root.left;
        }
    }
}
