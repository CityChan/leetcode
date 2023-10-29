class Solution {
    public boolean isPalindrome(String s) {
      // corner case: null, empty, 1 char
      if (s == null || s.length() <= 1) return true;
      s = s.trim();
      s = s.toLowerCase();
      
      int i = 0; 
      int j = s.length() - 1; 
      
      while (i < j) {
        char head = s.charAt(i);
        char tail = s.charAt(j);
        if (!Character.isLetterOrDigit(head)) {
          i++;
          continue;
        } 
        if (!Character.isLetterOrDigit(tail)) {
          j--;
          continue;
        }
        // two letters or digits are not matching 
        if (head != tail) {
          return false;
        }
        i++;
        j--;
      }
      return true;
    }
}
