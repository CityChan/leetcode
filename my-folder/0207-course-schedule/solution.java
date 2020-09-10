class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // adj list
        List<Integer>[] graph = new List[numCourses];
        for(int i=0;i<numCourses;i++){
            graph[i] = new ArrayList<>();
        }
        
        int[] indegree = new int[numCourses];
        for(int[] pair: prerequisites){
            // u -> v
            int u = pair[1];
            int v = pair[0];
            indegree[v]++;
            graph[u].add(v);
        }
        
        Queue<Integer> q = new LinkedList<>();
        // nodes with indegree being zero
        for(int i=0;i<numCourses;i++){
            if(indegree[i]==0){
                q.offer(i);
            }
        }
        List<Integer> sorted = new ArrayList<>();
        while(!q.isEmpty()){
            int node = q.poll();
            sorted.add(node);
            for(int next: graph[node]){
                indegree[next]--;
                if(indegree[next]==0){
                    q.offer(next);
                }
            }
            
        }
        return sorted.size()==numCourses;
    }
}
