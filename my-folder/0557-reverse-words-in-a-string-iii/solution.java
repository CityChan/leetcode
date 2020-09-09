class Solution {
    public String reverseWords(String s) {
        char[] arr = s.toCharArray();
        int i = 0;
        int j = 0;
        while(j<arr.length){
            while(j<arr.length&&arr[j]!=' '){
                j++;
            }
            // arr[j] is space or EOF
            reverse(arr, i, j-1);
            i = j+1;
            j = i;
        }
        return String.valueOf(arr);
    }
    
    private void reverse (char[]s, int start, int end){
        while(start<end){
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            start++;
            end--;
        }
    }
}
