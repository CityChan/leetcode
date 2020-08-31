class Solution {
    public int dietPlanPerformance(int[] calories, int k, int lower, int upper) {
        int points = 0;
        int t = 0;
        for(int i=0;i<calories.length;i++){
            t += calories[i];
            if(i>=k-1){
                if(i>k-1)
                    t -= calories[i-k];
                if(t<lower){
                    points--;
                }else if(t>upper){
                    points++;
                }
            }
        }
        
        return points;
    }
}
