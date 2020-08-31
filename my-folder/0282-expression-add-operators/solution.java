class Solution {    
    public List<String> addOperators(String num, int target) {
        List<String> ans = new ArrayList<>();
        if (num == null || num.length() == 0) return ans;
        backtrack(num, 0, (long) target, 0, 0, ans, new char[2*num.length()], 0);
        return ans;
    }
    
    private void backtrack(String num, int idx, long target, long val, long prev, List<String> ans, 
                          char[] res, int len) {
        // base case
        if (idx == num.length() && target == val) {
            ans.add(new String(res, 0, len));
        }
        
        int j = idx == 0 ? len : len+1;
        long x = 0;
        for (int i = idx; i < num.length(); i++) {
            x = x * 10 + (num.charAt(i) - '0');
            // skip leading zero
            if (x < 10 && i - idx > 0) break;
            
            res[j++] = num.charAt(i);
            if (idx == 0) {
                backtrack(num, i+1, target, val+x, x, ans, res, j);
                continue;
            }
            
            res[len] = '+';
            backtrack(num, i+1, target, val+x, x, ans, res, j);
            res[len] = '-';
            backtrack(num, i+1, target, val-x, -x, ans, res, j);
            res[len] = '*';
            backtrack(num, i+1, target, val-prev+prev*x, prev*x, ans, res, j);
        }
    }
    

}
