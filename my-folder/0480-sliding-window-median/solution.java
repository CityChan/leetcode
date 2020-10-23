class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int m = n - k + 1;
        double[] res = new double[m];
        
        PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> min = new PriorityQueue<>();
        for(int i=0;i<nums.length;i++){
            if(max.size()==0||nums[i]<=max.peek()){
                max.add(nums[i]);
            }else{
                min.add(nums[i]);
            }
            // System.out.println(max);
            // System.out.println(min);
            if(min.size()>max.size()){
                max.add(min.poll());
            }
            if(max.size()>min.size()+1){
                min.add(max.poll());
            }
            // System.out.println(max);
            // System.out.println(min);
            
            if(i>=k-1){
                if( k % 2 == 1 )
                    res[i - k + 1] = max.peek();
                else 
                    res[i - k + 1] = (max.peek()/2.0 +  min.peek()/2.0);
                int left = nums[i-k+1];
                if(left<=max.peek()){
                    max.remove(left);
                }else{
                    min.remove(left);
                }
                if(min.size()>max.size()){
                    max.add(min.poll());
                }
                if(max.size()>min.size()+1){
                    min.add(max.poll());
                }
            }

        }
        return res;
    }
}
