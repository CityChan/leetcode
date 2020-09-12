class Solution {
    public boolean isMatch(String s, String p) {
         if (p.length() == 0) return s.length() == 0;
    
    boolean[][] dp = new boolean[s.length()+1][p.length()+1];
    dp[0][0] = true;
    for (int i = 1; i <= p.length(); i++) {
      if (p.charAt(i-1) == '*' && dp[0][i-1]) {
        dp[0][i] = true;
      }
    }
    
    for (int i = 0; i < s.length(); i++) {
      for (int j = 0; j < p.length(); j++) {
        int row = i + 1;
        int col = j + 1;
        
        if (p.charAt(j) == '?') {
          dp[row][col] = dp[row-1][col-1];
        }
        
        if (p.charAt(j) == s.charAt(i)) {
          dp[row][col] = dp[row-1][col-1];
        }
        
        if (p.charAt(j) == '*') {
          dp[row][col] = dp[row][col-1] || dp[row-1][col-1] || dp[row-1][col];
        }
      }
      
    }
    return dp[s.length()][p.length()];
    
    }
}
