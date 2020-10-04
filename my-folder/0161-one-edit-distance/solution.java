class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int sLen = s.length();
        int tLen = t.length();
        
        // ensure s is shorter than or equals to t
        if(sLen>tLen){
            return isOneEditDistance(t, s);
        }
        
        // s<=t
        if(tLen-sLen>1){
            return false;
        }
        
        for(int i=0;i<sLen;++i){
            if(s.charAt(i)!=t.charAt(i)){
                // replace
                if(sLen==tLen){
                    return s.substring(i+1).equals(t.substring(i+1));
                }else{ // insert into s to get t
                    return s.substring(i).equals(t.substring(i+1)); 
                }
            }
        }
        
        // two possibilities: sLen==tLen or sLen+1==tLen
        
        return sLen+1==tLen;
    }
}
