class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        return atMostK(A, K) - atMostK(A, K-1);
    }
    
    
    private int atMostK(int[] A, int K){
        Map<Integer, Integer> map = new HashMap<>();
        int left = 0;
        int right = 0;
        int count = 0;
        for(;right<A.length;++right){
            if(!map.containsKey(A[right])){
                map.put(A[right], 1);
            }else{
                map.put(A[right], map.get(A[right])+1);
            }
            while(map.size()>K){
                map.put(A[left], map.get(A[left])-1);
                if(map.get(A[left])==0){
                    map.remove(A[left]);
                }
                left++;
            }
            count += right-left+1;
        }
        return count;
    }
}
