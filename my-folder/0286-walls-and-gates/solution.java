class Solution {
    public void wallsAndGates(int[][] rooms) {
        int m = rooms.length;
        if(m==0){
            return;
        }
        int n = rooms[0].length;
        Queue<Integer> q = new LinkedList<>();
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(rooms[i][j]==0){
                    q.offer(i*n+j);
                }
            }
        }
        while(!q.isEmpty()){
            int node = q.poll();
            int i = node / n;
            int j = node % n;
            if(i-1>=0 && rooms[i-1][j]==Integer.MAX_VALUE){
                rooms[i-1][j] = rooms[i][j] + 1;
                q.offer((i-1)*n+j);
            }
            if(i+1<rooms.length && rooms[i+1][j]==Integer.MAX_VALUE){
                rooms[i+1][j] = rooms[i][j] + 1;
                q.offer((i+1)*n+j);
            }
            if(j-1>=0 && rooms[i][j-1]==Integer.MAX_VALUE){
                rooms[i][j-1] = rooms[i][j] + 1;
                q.offer(i*n+j-1);
            }
            if(j+1<rooms[0].length && rooms[i][j+1]==Integer.MAX_VALUE){
                rooms[i][j+1] = rooms[i][j] + 1;
                q.offer(i*n+j+1);
            }
        }
    }
}
