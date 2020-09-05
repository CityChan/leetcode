class Solution {
    public String rearrangeString(String s, int k) {
        // corner case
        if (k == 0) return s;
        
        StringBuilder result = new StringBuilder();
        int[] map = new int[26];
        for (char c : s.toCharArray()) {
            map[c - 'a']++;
        }
        
        // a[0]: index; a[1]: frequence
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        for (int i = 0; i < 26; i++) {
            if (map[i] > 0) {
                pq.offer(new int[] {i, map[i]});
            }
        }
        
        LinkedList<int[]> queue = new LinkedList<>();
        
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            result.append((char) (curr[0] + 'a'));
            curr[1]--;
            queue.add(curr);
            
            if (queue.size() >= k) {
                int[] next = queue.poll();
                if (next[1] > 0) {
                    pq.offer(next);
                }
            }
        }
        
        return result.length() == s.length() ? result.toString() : "";
    }
}
