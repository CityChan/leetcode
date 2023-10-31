class Solution {
    public int longestPalindrome(String s) {
      // s should be a dict for 
      int[] dict = new int[256];
      for (char c : s.toCharArray()) {
        dict[c-'A']++;
      }
      
      int maxLen = 0;
      
      for (int count : dict) {
        if (count % 2 == 0) {
          maxLen += count;
        } else {
          // if the occurrence is even, then count-1 would be 
          maxLen += count-1;
        }
      }
      
      for (int count : dict) {
        if (count %2 != 0) {
          return maxLen+1;
        }
      }
      return maxLen;
    }
}
