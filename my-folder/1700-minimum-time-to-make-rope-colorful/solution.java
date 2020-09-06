class Solution {
    public int minCost(String s, int[] cost) {
        int n = s.length();
        if(n==1){
            return 0;
        }
        int minCost = 0;
        int i=1;
        while(i<n){
            int left = i-1;
            while(i<n&&s.charAt(i)==s.charAt(i-1)){
                i++;
            }
            if(i-left>1){ // has repeated letters
                int maxIndex = left;
                for(int j=left+1;j<i;j++){
                    if(cost[j]>cost[maxIndex]){
                        maxIndex = j;
                    }
                }
                for(int j=left;j<i;j++){
                    if(j!=maxIndex){
                        minCost += cost[j];
                    }
                }
                
            }
            i++;
            
        }
        
        return minCost;
    }
}
