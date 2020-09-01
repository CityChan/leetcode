class Solution {
    // bacc
    // b[acc
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int len = s.length();
        if(len<=k){
            return len;
        }
        int maxLen = 0;
        int left = 0;
        int right = 0;
        // char -> left most
        Map<Character, Integer> map = new LinkedHashMap<>();
        for(;right<len;right++){
            // System.out.println(map);
            char ch = s.charAt(right);
            if(map.containsKey(ch)){
                map.remove(ch);
            }
            map.put(ch, right);
            if(map.size()>k){
                  Map.Entry<Character, Integer> pair = map.entrySet().iterator().next();
                left = pair.getValue() + 1;
                map.remove(pair.getKey());
            }
            maxLen = Math.max(maxLen, right-left+1);
        }
        
        
        return maxLen;
    }
}
