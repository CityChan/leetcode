class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new List[numCourses];
        for(int i=0;i<numCourses;i++){
            graph[i] = new ArrayList<>();
        }
        int[] indegree = new int[numCourses];
        for(int[] pair: prerequisites){
            // u->v
            int u = pair[1];
            int v = pair[0];
            graph[u].add(v);
            indegree[v]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i=0;i<numCourses;++i){
            if(indegree[i]==0){
                q.add(i);
            }
        }
        int[] sorted = new int[numCourses];
        int i=0;
        while(!q.isEmpty()){
            int node = q.poll();
            sorted[i++] = node;
            for(int j: graph[node]){
                indegree[j]--;
                if(indegree[j]==0){
                    q.offer(j);
                }
            }
        }
        if(i==numCourses){
            return sorted;
        }
        return new int[0];
    }
}
