class Solution {
    public int[] gardenNoAdj(int N, int[][] paths) {
        // adjacency list
        List<Integer>[] graph = new List[N];
        for(int i=0;i<N;++i){
            graph[i] = new ArrayList<>();
        }
        for(int[] pairs: paths){
            graph[pairs[0]-1].add(pairs[1]-1);
            graph[pairs[1]-1].add(pairs[0]-1);
        }
        int[] flowers = new int[N];
        flowers[0] = 1;
        for(int i=1;i<N;++i){
            List<Integer> neighbors = graph[i];
            boolean[] used = new boolean[5];
            for(int neighbor: neighbors){
                used[flowers[neighbor]] = true;
            }
            for(int j=1;j<5;++j){
                if(!used[j]){
                    flowers[i] = j;
                    break;
                }
            }
        }
        
        return flowers;
    }
}
