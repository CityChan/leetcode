class Solution {
    public void reverseWords(char[] arr) {
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
