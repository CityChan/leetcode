class WordDictionary {
    TrieNode root;

    /** Initialize your data structure here. */
    public WordDictionary() {
        this.root = new TrieNode();
    }
    
    /** Adds a word into the data structure. */
    public void addWord(String word) {
        TrieNode cur = this.root;
        for(int i=0;i<word.length();++i){
            char ch = word.charAt(i);
            if(cur.children[ch-'a']==null){
                cur.children[ch-'a'] = new TrieNode();
            }
            cur = cur.children[ch-'a'];
        }
        cur.hasWord = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        return searchHelper(word.toCharArray(), 0, this.root);
    }
    
    private boolean searchHelper(char[] word, int start, TrieNode node){
        TrieNode cur = node;
        int i=start;
        while(i<word.length&&word[i]!='.'){
            if(cur.children[word[i]-'a']==null){
                return false;
            }
            cur = cur.children[word[i]-'a'];
            ++i;
        }
        if(i==word.length){
            return cur.hasWord;
        }
        for(int j=0;j<cur.children.length;j++){
            if(cur.children[j]!=null&&searchHelper(word, i+1, cur.children[j])){
                return true;
            }
        }
        return false;
    }
    
    class TrieNode{
        TrieNode[] children = new TrieNode[26];
        boolean hasWord = false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
