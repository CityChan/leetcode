class Solution {
    public int maxSubArray(int[] nums) {
      int currMaxSum = nums[0];
      int max = nums[0];
      
      for (int i = 1; i < nums.length; i++) {
        if (currMaxSum > 0) {
          currMaxSum += nums[i];
        } else {
          currMaxSum = nums[i];
        }
        max = Math.max(max, currMaxSum);
      }
      return max;
    }
}
