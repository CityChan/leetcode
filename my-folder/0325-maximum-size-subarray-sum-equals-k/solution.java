class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
              Map<Integer, Integer> map = new HashMap<>();
        int preSum = 0;
        int max = 0;
        map.put(0, -1);

        for (int i = 0; i < nums.length; i++) {
            preSum += nums[i];

            if (map.containsKey(preSum - k)) {
                max = Math.max(max, i - map.get(preSum - k));
            }

            if (!map.containsKey(preSum)) {
                map.put(preSum, i);
            }
        }
        return max;
    }
}
