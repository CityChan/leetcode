class Solution {
    public int search(int[] nums, int target) {
      
      int low = 0;
      int high = nums.length - 1;
      
      while (low + 1 < high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
          return mid;
        } else if (nums[mid] > target) {
          high = mid - 1;
        } else {
          low = mid + 1; 
        }
      }
      if (nums[low] == target) {
        return low; 
      } else if (nums[high] == target) {
        return high;
      }
      return -1;
    }
}
