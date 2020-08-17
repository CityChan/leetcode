class Solution {
    public int[] productExceptSelf(int[] nums) {
        // n > 1, no croner case checks 
        int n = nums.length;
        
        // left side product + initialize 
        int[] leftProduct = new int[n];
        leftProduct[0] = 1;
        for (int i = 1; i < n; i++) {
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
        }
        
        // right side product + initialize
        int[] rightProduct = new int[n];
        rightProduct[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
        }
        
        for (int i = 0; i < n; i++) {
            leftProduct[i] *= rightProduct[i];
        }
        
        return leftProduct;
    }
}
