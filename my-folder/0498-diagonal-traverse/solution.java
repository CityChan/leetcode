class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        int rows = matrix.length;
        if(rows == 0){
            return new int[0];
        }
        int cols = matrix[0].length;
        int total = rows * cols;
        int[] res = new int[total];
        
        int i=0;
        int j=0;
        for(int k=0;k<total;++k){
            res[k] = matrix[i][j];
            // even
            if((i+j)%2==0){ // up
                if(j==cols-1){
                    i++;
                }else if(i==0){
                    j++;
                }else{
                    i--;
                    j++;
                }
            }else{ // down
                if(i==rows-1){
                    j++;
                }else if(j==0){
                    i++;
                }else{
                    i++;
                    j--;
                }
            }
        }
        
        return res;
    }
}
