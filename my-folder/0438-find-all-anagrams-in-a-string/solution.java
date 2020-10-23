class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] counter = new int[26];
        
        for(int i=0;i<p.length();i++){
            counter[p.charAt(i)-'a']++;
        }
        int left = 0;
        int right = 0;
        int match = p.length();
        List<Integer> list = new ArrayList<>();
        
        while(right<s.length()){
            char ch = s.charAt(right);
            counter[ch-'a']--;
            if(counter[ch-'a']>=0){
                match--;
            }
            if(match==0){
                list.add(left);
            }
            if(right-left+1==p.length()){
                counter[s.charAt(left) - 'a']++;
                if(counter[s.charAt(left)-'a']>=1){
                    match++;
                }
                left++;
            }
            right++;
        }
        return list;
    }
}
