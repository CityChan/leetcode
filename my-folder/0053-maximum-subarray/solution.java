class Solution {
    public int maxSubArray(int[] nums) {
        int[] preSums = new int[nums.length];
        preSums[0] = nums[0];
        int max = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            if (preSums[i - 1] < 0) {
                preSums[i] = nums[i];
            } else {
                preSums[i] = nums[i] + preSums[i - 1];
            }
            if (preSums[i] > max) max = preSums[i];
        }
        return max;
    }
}
