class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++) {
            // skip duplicate
            if (i > 0 && nums[i - 1] == nums[i]) continue;
            int k =  - nums[i];
            int low = i + 1;
            int high = nums.length - 1;
            
            while (low < high) {
                if (nums[low] + nums[high] == k) {
                    
                    res.add(Arrays.asList(nums[i], nums[low], nums[high]));
                    
                    while (low < high && nums[low+1] == nums[low]) low++;
                    while (low < high && nums[high-1] == nums[high])high--;
                    
                    low++;
                    high--;
                } else if (nums[low] + nums[high] < k) {
                    low++;
                } else {
                    high--;
                }
            }
        }
        
        return res;
    }
}
