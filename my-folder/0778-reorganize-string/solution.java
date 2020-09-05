class Solution {
    public String reorganizeString(String S) {
        int[] hash = new int[26];
        for (char c : S.toCharArray()) hash[c - 'a']++;
        
        int max = 0, letter = 0;
        for (int i = 0; i < 26; i++) {
            if (hash[i] > max) {
                max = hash[i];
                letter = i;
            }
        }
        
        if (max > (S.length() + 1) / 2) return "";
        
        char[] res = new char[S.length()];
        int index = 0;
        while (hash[letter] > 0) {
            res[index] = (char) (letter + 'a');
            index += 2;
            hash[letter]--;
        }
        
        for (int i = 0; i < 26; i++) {
            while (hash[i] > 0) {
                if (index >= res.length) index = 1;
                
                res[index] = (char) (i + 'a');
                index += 2;
                hash[i]--;
            }
        }
        
        return String.valueOf(res);
    }
}
