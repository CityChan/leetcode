class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        if(m==0){
            return 0;
        }
        int n = grid[0].length;
        UnionFind uf = new UnionFind(grid);
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(grid[i][j]=='1'){
                    grid[i][j] = '2';
                    if(i-1>=0&&grid[i-1][j]=='1'){
                        uf.union(i*n+j , (i-1)*n+j);
                    }
                    if(i+1<m&&grid[i+1][j]=='1'){
                        uf.union(i*n+j , (i+1)*n+j);
                    }
                    if(j-1>=0&&grid[i][j-1]=='1'){
                        uf.union(i*n+j , i*n+j-1);
                    }
                    if(j+1<n&&grid[i][j+1]=='1'){
                        uf.union(i*n+j , i*n+j+1);
                    }
                }
            }
        }
        return uf.count;
    }
    
    class UnionFind {
        int[] parents;
        int[] ranks;
        int count = 0;
        
        public UnionFind(char[][] grid){
            int m = grid.length;
            int n = grid[0].length;
            parents = new int[m*n];
            ranks = new int[m*n];
            for(int i=0;i<m;++i){
                for(int j=0;j<n;++j){
                    if(grid[i][j]=='1'){
                        parents[i*n + j] = i*n + j;
                        count++;
                    }
                }
            }
        }
        
        int root(int i){
            while(parents[i]!=i){
                parents[i] = parents[parents[i]]; // path compression
                i = parents[i];
            }
            return i;
        }
        
        void union(int i, int j){
            int root1 = root(i);
            int root2 = root(j);
            if(root1!=root2){
                if(ranks[root1]>ranks[root2]){
                    parents[root2] = root1;
                }else if(ranks[root1]<ranks[root2]){
                    parents[root1] = root2;
                }else{ // equal
                    parents[root2] = root1;
                    ranks[root1]++;
                }
                count--;
            }
        }
        
    }
}
