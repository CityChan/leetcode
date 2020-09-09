class Solution {
    // [2, 5, 2, 1, 2]
    // [1, 2, 2, 2, 5] target:5 
    // 
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
       List<List<Integer>> res = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        
        Arrays.sort(candidates);
        
        backtrack(res, tmp, 0, candidates, target);
        
        return res;
    }
    
    private void backtrack(List<List<Integer>> res, List<Integer> tmp, int start, int[] candidates, int target) {
        
        if (target < 0) return;
        
        if (target == 0) {
            res.add(new ArrayList<Integer>(tmp));
            return;
        }
        
        for (int i = start; i < candidates.length; i++) {
            // last one was the same as current, has been dfsed 
            if (i > start && candidates[i - 1] == candidates[i]) continue;
            
            tmp.add(candidates[i]);
            
            // i+1 不可以同一个element使用多次，但出现了多次的element可以都依次加进去。
            backtrack(res, tmp, i+1, candidates, target - candidates[i]);
            
            tmp.remove(tmp.size() - 1);
        }
    }
}
