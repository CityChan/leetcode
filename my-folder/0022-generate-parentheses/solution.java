class Solution {
    
    List<String> res = new ArrayList<>();
    
    public List<String> generateParenthesis(int n) {
        // constrcut a string object out of a char array of length 2*n from current index 
        // and contains well-formed parentheses. 
        backtrack(new char[n*2], 0, 0, 0, n);
        return res;
    }
    
    private void backtrack(char[] arr, int currIndex, int open, int close, int max) {
        if (close == max) {
            res.add(new String(arr));
            return;
        }
        
        if (open < max) {
            arr[currIndex] = '(';
            backtrack(arr, currIndex+1, open+1, close, max);
        }
        
        if (close < open) {
            arr[currIndex] = ')';
            backtrack(arr, currIndex+1, open, close+1, max);
        }
    }
}
