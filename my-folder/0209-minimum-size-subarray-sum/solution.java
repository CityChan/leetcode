class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int left = 0;
        int right = 0;
        int curSum = 0;
        int minLen = nums.length + 1;
        for(;right<nums.length;++right){
            curSum +=nums[right];
            while(curSum>=s){
                minLen = Math.min(minLen, right-left+1);
                curSum -= nums[left++];
            }
        }
        
        return minLen==nums.length+1? 0:minLen;
    }
}
