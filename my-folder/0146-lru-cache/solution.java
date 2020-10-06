class LRUCache {
    
    // head - most recently used
    // tail - least recently used
    class Node{
        int key;
        int value;
        Node pre;
        Node next;
    }
    int capacity;
    HashMap<Integer, Node> cache = new HashMap<>();
    Node head;
    Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head = new Node();
        tail = new Node();
        head.next = tail;
        tail.pre = head;
    }
    
    public int get(int key) {
        if(cache.containsKey(key)){
            Node node = cache.get(key);
            // move to head
            moveToHead(node);
            return node.value;
        }
        return -1;
        
    }
    
    private void moveToHead(Node node){
        // remove
        remove(node);
        // add to head
        addToHead(node);
    }
    
    private void remove(Node node){
        node.pre.next = node.next;
        node.next.pre = node.pre;
    }
    
    private void addToHead(Node node){
        node.pre = head;
        node.next = head.next;
        head.next.pre = node;
        
        head.next = node;
    }
    
    public void put(int key, int value) {
        if(cache.containsKey(key)){
            // update value;
            Node node = cache.get(key);
            node.value = value;
            // move to head;
            moveToHead(node);
        }else{
            Node newNode = new Node();
            newNode.key = key;
            newNode.value = value;
            
            cache.put(key, newNode);
            addToHead(newNode);
            
            // remove from tail
            if(cache.size()>capacity){
                Node toRemove = tail.pre;
                remove(toRemove);
                cache.remove(toRemove.key);
            }
            
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
