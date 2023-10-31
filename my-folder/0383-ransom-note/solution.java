class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
      if (magazine.length() < ransomNote.length()) return false; 
      
      int[] counter = new int[26];
      for (char c : magazine.toCharArray()) {
        counter[c - 'a']++;
      }
      
      for (char c : ransomNote.toCharArray()) {
        counter[c - 'a']--;
      }
      
      for (int count : counter) {
        if (count < 0) return false;
      } 
      return true;
    }
}
