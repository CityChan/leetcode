class Solution {
    public String alienOrder(String[] words) {
        if (words == null || words.length == 0) return "";
        // build a graph for the edges and vertexes 
        Map<Character, Set<Character>> map = new HashMap<>();
        Map<Character, Integer> degree = new HashMap<>();
        
        for (String word : words) {
            for (char c : word.toCharArray()) {
                degree.put(c, 0);
            }
        }
        
        for (int i = 0; i < words.length - 1; i++) {
            String curr = words[i];
            String next = words[i + 1];
            // corner case check 
            if (curr.length() > next.length() && curr.startsWith(next)) return "";
            int len = Math.min(curr.length(), next.length());
            for (int j = 0; j < len; j++) {
                char first = curr.charAt(j);
                char second = next.charAt(j);
                // different pairs compare once and break 
                if (first != second) {
                    Set<Character> set = new HashSet<>();
                    if (map.containsKey(first)) {
                        set = map.get(first);
                    }
                    if (!set.contains(second)) {
                        set.add(second);
                        map.put(first, set);
                        degree.put(second, degree.get(second) + 1);
                    }
                    break;
                } 
            }
        }
        
        Queue<Character> queue = new LinkedList<>();
        for (char c : degree.keySet()) {
            if (degree.get(c) == 0) {
                queue.add(c);
            }
        }
        
        StringBuilder sb = new StringBuilder();
        
        while (!queue.isEmpty()) {
            char c = queue.remove();
            sb.append(c);
            
            if (map.containsKey(c)) {
                // 每个可以到达的点的Degree - 1
                for (char v : map.get(c)) {
                    degree.put(v, degree.get(v) - 1);
                    if (degree.get(v) == 0) {
                        queue.add(v);
                    }
                }
            }
        }
        
        if (sb.length() != degree.size()) return "";
        
        return sb.toString();
    }
}
