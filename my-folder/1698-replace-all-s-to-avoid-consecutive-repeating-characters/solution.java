class Solution {
    public String modifyString(String s) {
        char[] arr = s.toCharArray();
        
        for(int i=0;i<arr.length;i++){
            if(arr[i]=='?'){
                int candidate = 0;
                while(i>0&&arr[i-1]-'a'==candidate||i<arr.length-1&&arr[i+1]-'a'==candidate){
                    candidate = (candidate + 1)%26;
                }
                arr[i] = (char)('a' + candidate);
            }
        }
        
        
        return String.valueOf(arr);
    }
}
