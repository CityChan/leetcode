class Solution {
    public String reverseWords(String s) {
        char[] arr = s.toCharArray();
        // reverse the whole string
        reverse(arr, 0, arr.length-1);
        // reverse each word
        int start = 0;
        while(start<arr.length){
            while(start<arr.length&&arr[start]==' '){
                start++;
            }
            int end = start + 1;
            while(end<arr.length&&arr[end]!=' '){
                end++;
            }
            // [start,end) 
            reverse(arr, start, end-1);
            start = end;
        }
        // "world hellollo "
        int i = 0;
        int j = 0;
        while(j<arr.length){
            while(j<arr.length&&arr[j]==' '){
                j++;
            }
            if(j==arr.length){
                break;
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
    
    private void reverse(char[] arr, int start, int end){
        while(start<end){
            char tmp = arr[start];
            arr[start] = arr[end];
            arr[end] = tmp;
            start++;
            end--;
        }
    }
}
