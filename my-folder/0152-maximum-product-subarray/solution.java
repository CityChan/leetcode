class Solution {
    public int maxProduct(int[] nums) {
        int preMax = nums[0];
        int preMin = nums[0];
        int max = preMax;
        int end = 0;
        for(int i=1;i<nums.length;i++){
            int tempMax = Math.max(nums[i], Math.max(nums[i]*preMax, nums[i]*preMin));
            preMin = Math.min(nums[i], Math.min(nums[i]*preMax, nums[i]*preMin));
            preMax = tempMax;
            
            if(preMax>max){
                max = preMax;
                end = i;
            }
        }
        // int product = 1;
        // int start = end;
        // for(int i=end;i>=0;i--){
        //     product *=nums[i];
        //     if(product==max){
        //         start = i;
        //         break;
        //     }
        // }
        // for(int i=start;i<=end;i++){
        //     System.out.println(nums[i]);
        // }
        
        return max;
    }
}
