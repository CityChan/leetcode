class Solution {
    public int majorityElement(int[] nums) {
      int element = 0;
      int count = 0; 
      for (int num : nums) {
        if (element == num) {
          count += 1; 
        } else if (count == 0) {
          element = num;
          count = 1;
        } else {
          count -= 1; 
        }
      }
      return element;
    }
}
