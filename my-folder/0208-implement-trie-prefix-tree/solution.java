class Trie {
    TrieNode root;

    /** Initialize your data structure here. */
    public Trie() {
        this.root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
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
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode cur = this.root;
        for(int i=0;i<word.length();++i){
            char ch = word.charAt(i);
            if(cur.children[ch-'a']==null){
                return false;
            }
            cur = cur.children[ch-'a'];
        }
        return cur.hasWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode cur = this.root;
        for(int i=0;i<prefix.length();++i){
            char ch = prefix.charAt(i);
            if(cur.children[ch-'a']==null){
                return false;
            }
            cur = cur.children[ch-'a'];
        }
        return true;
    }
    
    class TrieNode{
        TrieNode[] children = new TrieNode[26];
        boolean hasWord = false;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
