class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        // Construct a map for each char and the indea
        Map<Character, Integer> dict = new HashMap<>();
        for (int i = 0; i < order.length(); i++) {
            dict.put(order.charAt(i), i);
        }
        
        for (int i = 0; i < words.length - 1; i++) {
            String word1 = words[i];
            String word2 = words[i + 1];
            
            if (!isSorted(word1, word2, dict)) {
                return false;
            } else {
                continue;
            }
        }
        return true;
    }
    
    private boolean isSorted(String word1, String word2, Map<Character, Integer> dict) {
        int len = Math.min(word1.length(), word2.length());
        for (int i = 0; i < len; i++) {
            char char1 = word1.charAt(i);
            char char2 = word2.charAt(i);
            
            if (char1 != char2) {
                // different chars, just compare the order of them
                return dict.get(char1) < dict.get(char2);
            } else {
                // same chars, continue to compare next 
                continue;
            }
        }
        
        // if s1 has a longer length and all the same chars till now
        if (word1.length() > word2.length()) {
            return false;
        }
        return true;
    }
}
