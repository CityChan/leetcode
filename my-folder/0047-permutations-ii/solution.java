class Solution {
    // [1, 1, 2] 
    // [f, f, f]
    // [1, t, 1, t, 2, t]
    // [1, t, 1, f, 2, f]
    // [1 t, 2 t, 1 t]
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        boolean[] visited = new boolean[nums.length];
        
        Arrays.sort(nums);
        
        helper(res, tmp, visited, nums);
        
        return res;
    }
    
    private void helper(List<List<Integer>> res, List<Integer> tmp, boolean[] visited, int[] nums) {
        
        if (tmp.size() == nums.length) {
            res.add(new ArrayList<Integer>(tmp));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) continue;
            
            if (i > 0 && nums[i - 1] == nums[i] && !visited[i - 1]) continue;
            
            tmp.add(nums[i]);
            visited[i] = true;
            
            helper(res, tmp, visited, nums);
            
            tmp.remove(tmp.size() - 1);
            visited[i] = false;
        }
    }
    
}
