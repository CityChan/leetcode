class Solution {
    public int[][] intervalIntersection(int[][] A, int[][] B) {
        List<int[]> ans = new ArrayList<>();
        int i = 0, j = 0;
        while (i < A.length && j < B.length) {
            int low = Math.max(A[i][0], B[j][0]);
            int high = Math.min(A[i][1], B[j][1]);
            if (low <= high) {
                ans.add(new int[] {low, high});
            }
            
            if (A[i][1] < B[j][1]) {
                i++;
            } else {
                j++;
            }
        }
        
        return ans.toArray(new int[ans.size()][]);
    }
}
