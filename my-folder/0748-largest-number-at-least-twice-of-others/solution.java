class Solution {
    public int dominantIndex(int[] nums) {
        int n = nums.length;
        if(n==1){
            return 0;
        }
        int maxIndex = 0;
        int secondMaxIndex = -1;
        for(int i=1;i<n;i++){
            if(nums[i]>nums[maxIndex]){
                secondMaxIndex = maxIndex;
                maxIndex = i;
            }else if(secondMaxIndex==-1||nums[i]>nums[secondMaxIndex]){
                secondMaxIndex = i;
            }
        }
        
        if(nums[maxIndex] >= nums[secondMaxIndex]*2){
            return maxIndex;
        }
        return -1;
    }
}
