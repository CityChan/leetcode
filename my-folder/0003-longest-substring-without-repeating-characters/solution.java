class Solution {
    // abcbad
    // ab[cbad]
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        int left = 0;
        // char -> right most index
        Map<Character, Integer> map = new HashMap<>();
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if(map.containsKey(ch)){
                left = Math.max(left, map.get(ch) + 1);
            }
            map.put(ch, i);
            maxLen = Math.max(maxLen, i-left+1);
        }
        return maxLen;
    }
}
