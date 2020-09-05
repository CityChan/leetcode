class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;
        if(n==0){
            return -1;
        }
        int sum = 0;
        for(int num: nums){
            sum += num;
        }
        
        int left = 0;
        for(int i=0;i<n;i++){
            int right = sum-left-nums[i];
            if(left==right){
                return i;
            }
            left += nums[i];
        }
        return -1;
    }
}
