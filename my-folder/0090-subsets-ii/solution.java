class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        
        // popular all duplicates together, return non=descending results
        Arrays.sort(nums);
        
        helper(res, temp, 0, nums);
        return res;
    }
    
    private void helper(List<List<Integer>> res, List<Integer> tmp, int start, int[] nums) {
        res.add(new ArrayList<Integer>(tmp));
        
        for (int i = start; i < nums.length; i++) {
            //deduplicate 
            if (i > start && nums[i - 1] == nums[i]) {
                continue;
            }
            
            tmp.add(nums[i]);
            helper(res, tmp, i+1, nums);
            tmp.remove(tmp.size() - 1);
        }
    }
}
