class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        int rows = matrix.length;
        if(rows==0){
            return res;
        }
        int cols = matrix[0].length;
        int r1 = 0;
        int r2 = rows-1;
        int c1 = 0;
        int c2 = cols-1;
        while(r1<=r2&&c1<=c2){
            // right
            for(int i=c1;i<=c2;++i){
                res.add(matrix[r1][i]);
            }
            r1++;
            
            // down
            for(int i=r1;i<=r2;++i){
                res.add(matrix[i][c2]);
            }
            c2--;
            
            if(r1>r2||c1>c2){
                break;
            }
            // left
            for(int i=c2;i>=c1;--i){
                res.add(matrix[r2][i]);
            }
            r2--;
            
            // up
            for(int i=r2;i>=r1;--i){
                res.add(matrix[i][c1]);
            }
            c1++;
        }
        
        return res;
    }
}
