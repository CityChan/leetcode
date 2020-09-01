class Solution {
    public int totalFruit(int[] tree) {
        // 2 baskets
        // Map<Integer, Integer> count = new HashMap<>();
        int i = 0, j;
        int maxCount = 0;
        int curMax = 0;
        int lastFruit = -1;
        int secondLastFruit = -1;
        int lastFruitCount = 0;
        for (j = 0; j < tree.length; ++j) {
            int cur = tree[j];
            if(cur==lastFruit){
                curMax++;
                lastFruitCount++;
            }else if(cur==secondLastFruit){
                curMax++;
                secondLastFruit = lastFruit;
                lastFruit = cur;
                lastFruitCount=1;
            }else{
                curMax = lastFruitCount + 1;
                secondLastFruit = lastFruit;
                lastFruit = cur;
                lastFruitCount=1;
            }
            maxCount = Math.max(maxCount, curMax);
            
        }
        return maxCount;
    }
}
