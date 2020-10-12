class Solution {
    public boolean isNumber(String s) {
        if (s == null || s.length() == 0) {
      return false;
    }
    s = s.trim();
    int n = s.length();
    boolean hasDigit = false;
    boolean hasPoint = false;
    boolean hasE = false;
    for (int i = 0; i < n; i++) {
      char c = s.charAt(i);
      if (c >= '0' && c <= '9') { // is digit
        hasDigit = true;
      } else if (c == '.') {
        if (hasPoint || hasE) {
          return false;
        }
        hasPoint = true;
        // hasDigit = false;
      } else if (c == '-' || c == '+') {
        if (i != 0 && s.charAt(i - 1) != 'e') {
          return false;
        }
      } else if (c == 'e') {
        if(hasE || !hasDigit){
          return false;
        }
        hasE = true;
        hasDigit = false;
      } else { // other characters
        return false;
      }
    }
    return hasDigit;
    }
}
