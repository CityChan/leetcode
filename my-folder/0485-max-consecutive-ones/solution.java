class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int cur = 0;
        for(int num: nums){
            if(num==1){
                cur++;
            }else{
                max = Math.max(max, cur);
                cur = 0;
            }
        }
        max = Math.max(max, cur);
        return max;
    }
}
