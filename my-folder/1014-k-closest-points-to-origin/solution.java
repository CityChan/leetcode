class Solution {
    public int[][] kClosest(int[][] points, int k) {
      int n = points.length;
      int[] dists = new int[n];
      for (int i = 0; i < n; i++) {
        dists[i] = getDistance(points[i]);
      }
      
      // ascending order
      Arrays.sort(dists);
      int distK = dists[k-1];
      
      int[][] ans = new int[k][2];
      int t = 0;
      for (int i = 0; i < n; i++) {
        if (getDistance(points[i]) <= distK) {
          ans[t++] = points[i];
        }
      }
      return ans;   
    }
  
    private int getDistance(int[] point) {
      return point[0] * point[0] + point[1] * point[1];
    }
}
