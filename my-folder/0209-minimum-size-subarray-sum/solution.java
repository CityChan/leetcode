class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = 0;
        int sum = 0;
        int minLen = n + 1;
        while(right<n){
            sum += nums[right];
            while(sum>=s){
                minLen = Math.min(minLen, right - left + 1);
                sum -= nums[left++];
            }
            right++;
        }
        return minLen == n+1? 0: minLen;
    }
}
