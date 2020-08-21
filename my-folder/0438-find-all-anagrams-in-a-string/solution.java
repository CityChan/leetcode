class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        
        if (p.length() > s.length()) return ans;
        
        Map<Character, Integer> reference = new HashMap<>();
        for (char c : p.toCharArray()) {
            reference.put(c, reference.getOrDefault(c, 0) + 1);
        }
        
        Map<Character, Integer> map = new HashMap<>();
        int start = 0, end = 0, match = 0;
        
        while (end < s.length()) {
            char c1 = s.charAt(end);
            if (reference.containsKey(c1)) {
                map.put(c1, map.getOrDefault(c1, 0) + 1);
                if (map.get(c1).equals(reference.get(c1))) match++;
            }
            
            while (match == reference.size()) {
                if (end - start + 1 == p.length()) {
                    ans.add(start);
                }
                
                char c2 = s.charAt(start);
                if (reference.containsKey(c2)) {
                    map.put(c2, map.get(c2) - 1);
                    if (map.get(c2) < reference.get(c2)) {
                        match--;
                    }
                }
                start++;
            }
            end++;
        }
        return ans;
    }
}
