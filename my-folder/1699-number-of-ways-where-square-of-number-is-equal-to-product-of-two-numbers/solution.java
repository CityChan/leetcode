class Solution {
    public int numTriplets(int[] nums1, int[] nums2) {
        Map<Long, Integer> map1 = new HashMap<>();
        for(long num:nums1){
            map1.put(num*num, map1.getOrDefault(num*num, 0) + 1);
        }
        
        Map<Long, Integer> map2 = new HashMap<>();
        for(long num:nums2){
            map2.put(num*num, map2.getOrDefault(num*num, 0) + 1);
        }
        // System.out.println(map1);
        
        int count = 0;
        for(int i=0;i<nums2.length;i++){
            for(int j=i+1;j<nums2.length;j++){
                if(map1.containsKey((long)nums2[i]*nums2[j])){
                    count += map1.get((long)nums2[i]*nums2[j]);
                }
            }
        }
        // System.out.println(count);
        
        for(int i=0;i<nums1.length;i++){
            for(int j=i+1;j<nums1.length;j++){
                if(map2.containsKey((long)nums1[i]*nums1[j])){
                    count += map2.get((long)nums1[i]*nums1[j]);
                }
            }
        }
        return count;
    }
}
