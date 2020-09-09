class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
     
        
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        
        backtrack(res, tmp, 1, k, n);
        
        return res;
    }
    
    private void backtrack(List<List<Integer>> res, List<Integer> tmp, int start, int k, int n) {
        if (n < 0) return;
        // base case
        if (tmp.size() == k && n == 0) {
            res.add(new ArrayList<Integer>(tmp));
            return;
        }
        
        for (int i = start; i <= 9; i++) {
            tmp.add(i);
            
            backtrack(res, tmp, i+1, k, n - i);
            
            tmp.remove(tmp.size() - 1);
        }
    }
    
}
