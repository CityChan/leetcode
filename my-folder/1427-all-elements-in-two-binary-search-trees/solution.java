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
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        Deque<TreeNode> s1 = new LinkedList<>();
        Deque<TreeNode> s2 = new LinkedList<>();
        helper(s1, root1);
        helper(s2, root2);
        
        List<Integer> ans = new ArrayList<>();
        while(!s1.isEmpty()||!s2.isEmpty()){
            Deque<TreeNode> stack = s1.isEmpty()? s2: (s2.isEmpty()? s1:(s1.peek().val<=s2.peek().val? s1:s2));
            TreeNode node = stack.pop();
            ans.add(node.val);
            helper(stack, node.right);
        }
        
        return ans;
    }
    
    
    private void helper(Deque<TreeNode> stack, TreeNode root){
        while(root!=null){
            stack.push(root);
            root = root.left;
        }
    }
}
