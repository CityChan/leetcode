class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> map = new HashMap<>();
        int count = 0;
        for(List<String> pair: tickets){
            String from = pair.get(0);
            String to = pair.get(1);
            
            map.putIfAbsent(from, new PriorityQueue<>());
            map.get(from).add(to);
            // ++count;
        }
        
        String src = "JFK";
        LinkedList<String> res = new LinkedList<>();
        dfs(map, src, res);
        return res;
    }
    
    private void dfs(Map<String, PriorityQueue<String>> map, String src, LinkedList<String> res){
        if(map.containsKey(src)){
            PriorityQueue<String> q = map.get(src);
            while(!q.isEmpty()){
                dfs(map, q.poll(), res);
            }
        }
        res.addFirst(src);
    }
}
