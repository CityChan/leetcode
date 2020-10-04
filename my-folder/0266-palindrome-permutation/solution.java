class Solution {
    public boolean canPermutePalindrome(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for(int i=0;i<s.length();++i){
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0)+1);
        }
        boolean oddFound = false;
        for(char c: map.keySet()){
            if(map.get(c)%2!=0){
                if(oddFound){
                    return false;
                }
                oddFound = true;
            }
        }
        return true;
    }
}
