class Solution {
    public int longestSubstring(String s, int k) {
        if(s==null||s.length()==0){
            return 0;
        }
        int n = s.length();
        char[] str = s.toCharArray();
        int max = 0;
        
        // try with assumption that there are 1...26 unique letters in the substring
        for(int u=1;u<=26;++u){ 
            int[] count = new int[26];
            int i = 0; // left pointer
            int j = 0;
            int uniqueCount = 0;
            int KCount = 0;
            while(j<n){
                if(uniqueCount<=u){
                    count[str[j]-'a']++;
                    if(count[str[j]-'a']==1){
                        uniqueCount++;
                    }
                    if(count[str[j]-'a']==k){
                        KCount++;
                    }
                    j++;
                }else{
                    count[str[i]-'a']--;
                    if(count[str[i]-'a']==k-1){
                        KCount--;
                    }
                    if(count[str[i]-'a']==0){
                        uniqueCount--;
                    }
                    i++;
                }
                if(uniqueCount==u&&uniqueCount==KCount){
                    max = Math.max(j-i, max);
                }
            }
        }
        
        return max;
    }
}
