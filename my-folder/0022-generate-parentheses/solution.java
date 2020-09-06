class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        helper(res, new StringBuilder(), 0, 0, n);
        return res;
    }
    
    private void helper(List<String> res, StringBuilder sb, int open, int close, int max) {
        
        // base case
        if (sb.length() == max * 2) {
            res.add(sb.toString());
            return;
        }
        
        if (open < max) {
            sb.append('(');
            helper(res, sb, open+1, close, max);
            sb.setLength(sb.length() - 1);
        }
        
        if (close < open) {
            sb.append(')');
            helper(res, sb, open, close+1, max);
            sb.setLength(sb.length() - 1);
        }
    }
}
