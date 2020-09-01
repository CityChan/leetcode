class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int len = s.length();
        if(len<=2){
            return len;
        }
        int maxLen = 0;
        // char -> occurrences
        // Map<Character, Integer> map = new HashMap<>();
        int left = 0;
        int right = 0;
        char lastChar = '\0';
        char secondLastChar = '\0';
        int lastCharCount = 0;
        int curMax = 0;
        for(;right<len;right++){
            char ch = s.charAt(right);
            if(ch==lastChar){
                curMax++;
                lastCharCount++;
            }else if(ch==secondLastChar){
                curMax++;
                secondLastChar = lastChar;
                lastChar = ch;
                lastCharCount = 1;
            }else{
                curMax = lastCharCount + 1;
                secondLastChar = lastChar;
                lastChar = ch;
                lastCharCount = 1;
            }
            maxLen = Math.max(maxLen, curMax);
        }
        
        return maxLen;
    }
}
