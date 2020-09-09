class Solution {
    public String reverseWords(String s) {
        char[] arr = s.toCharArray();
        reverse(arr, 0, arr.length-1);
        // reverse each word
        int start = 0;
        while(start<arr.length){
            while(start<arr.length&&arr[start]==' '){
                start++;
            }
            if(start==arr.length){
                break;
            }
            int end = start;
            while(end<arr.length&&arr[end]!=' '){
                end++;
            }
            reverse(arr, start, end-1);
            start = end;
        }
        // remove multiple space
        int i=0;
        int j=0;
        while(j<arr.length){
            while(j<arr.length&&arr[j]==' '){
                j++;
            }
            while(j<arr.length&&arr[j]!=' '){
                arr[i++] = arr[j++];
            }
            while(j<arr.length&&arr[j]==' '){
                j++;
            }
            if(j<arr.length){
                arr[i++] = ' ';
            }
        }
        
        return String.valueOf(arr, 0, i);
    }
    
    
    private void reverse(char[] s, int start, int end){
        while(start<end){
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            start++;
            end--;
        }
    }
}
