class Solution {
    public int monotoneIncreasingDigits(int N) {
        if(N<10){
            return N;
        }
        char[] arr = String.valueOf(N).toCharArray();
        int n = arr.length;
        int marker = n;
        for(int i=n-1;i>0;--i){
            if(arr[i]<arr[i-1]){
                arr[i-1]--;
                marker = i;
            }
        }
        for(int i=marker;i<n;i++){
            arr[i] = '9';
        }
        return Integer.parseInt(String.valueOf(arr));
    }
}
