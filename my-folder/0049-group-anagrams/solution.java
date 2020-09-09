class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        
        if (strs == null || strs.length == 0) return res;
        
        Map<String, List<String>> map = new HashMap<>();
        for (String s: strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String anagram = String.valueOf(chars);
            
            if (!map.containsKey(anagram)) {
                map.put(anagram, new ArrayList<String>());
            } 
            map.get(anagram).add(s);
        }
        
        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            res.add(entry.getValue());
        }
        return res;
    }
}
