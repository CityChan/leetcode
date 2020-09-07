class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        helper(res, list, 0, nums);
        return res;
    }
    
    private void helper(List<List<Integer>> res, List<Integer> list, int start, int[] nums) {
        res.add(new ArrayList<Integer>(list));
        
        for (int i = start; i < nums.length; i++) {
            list.add(nums[i]);
            helper(res, list, i+1, nums);
            list.remove(list.size() - 1);
        }
    }
}
