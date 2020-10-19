class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> set = new HashSet<>(wordList);
        Set<String> visited = new HashSet<>();
        Queue<String> q = new LinkedList<>();
        q.offer(beginWord);
        visited.add(beginWord);
        // curString -> parent string
        Map<String, String> map = new HashMap<>();
        
        int len = 1;
        while(!q.isEmpty()){
            int size = q.size();
            for(int i=0;i<size;i++){
                String word = q.poll();
                if(word.equals(endWord)){
                    // Deque<String> stack = new ArrayDeque<>();
                    // stack.push(word);
                    // String parent = map.get(word);
                    // while(!parent.equals(beginWord)){
                    //     stack.push(parent);
                    //     parent = map.get(parent);                
                    // }
                    // stack.push(parent);
                    // while(!stack.isEmpty()){
                    //     System.out.println(stack.pop());
                    // }
                   
                    return len;
                }
                char[] chars = word.toCharArray();
                
                for(int j=0;j<chars.length;j++){
                    char old = chars[j];
                    for(int c='a';c<='z';c++){
                        chars[j] = (char)c;
                        String newWord = new String(chars);
                        if(set.contains(newWord)&&!visited.contains(newWord)){
                            q.offer(newWord);
                            visited.add(newWord);
                            map.put(newWord, word);
                        }
                        chars[j] = old;
                    }
                }
            }
            ++len;
        }
        return 0;
        
    }
}
