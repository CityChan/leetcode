class Solution {
    public int[][] kClosest(int[][] points, int K) {
        if (points == null || points.length <= K) return points;
        
        // max heap of each point int[] 
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (p1, p2) -> (p2[0] * p2[0] + p2[1] * p2[1] - p1[0] * p1[0] - p1[1] * p1[1])
        );
        
        for (int[] p : points) {
            pq.offer(p);
            if (pq.size() > K) {
                pq.poll();
            }
        }
        
        int[][] res = new int[K][2];
        while (K > 0) {
            res[--K] = pq.poll();
        }
        
        return res;
    }
}
