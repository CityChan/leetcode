class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> res = new ArrayList<>();
        
        if (s == null) return res;
        
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        visited.add(s);
        queue.add(s);
        boolean found = false;
        
        while (!queue.isEmpty()) {
            s = queue.poll();
            
            if (isValid(s)) {
                res.add(s);
                found = true;
            }
            
            if (found) continue;
            
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) != '(' && s.charAt(i) != ')') continue;
                String t = s.substring(0, i) + s.substring(i+1);
                if (!visited.contains(t)) {
                    queue.add(t);
                    visited.add(t);
                } 
            }
        }
        return res;
    }
    
    private boolean isValid(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') count++;
            if (c == ')') {
                if (count == 0) return false;
                count--;
            }
        }
        return count == 0;
    }
}
