class Solution {
    // backtracking 
    // sort helps so that we search from smaller to larger 
    // [2, 3, 6, 7]  target: 7=> from index 0 -> 2
    // [2] -> 5 -> [2, 3] -> 2 how to check if 2 is used or not? => using a set 
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        
        Arrays.sort(candidates);
        
        backtrack(res, new ArrayList<Integer>(), 0, candidates, target);
        
        return res;
    }
    
    private void backtrack(List<List<Integer>> res, List<Integer> tmp, int start, int[] candidates, int target) {
        if (target < 0) return;
        
        if (target == 0) {
            res.add(new ArrayList<Integer>(tmp));
            return;
        }
        
        for (int i = start; i < candidates.length; i++) {
            tmp.add(candidates[i]);
            
            backtrack(res, tmp, i, candidates, target - candidates[i]);
            
            tmp.remove(tmp.size() - 1);
        }
    }
}
