class Node {
    int key, value;
    Node prev, next;

    Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

// design the class in the most optimal way
class LRUCache {
    // Constructor for initializing the cache capacity with the given value.
    private int capacity;
    private HashMap<Integer, Node> cache;
    private Node head, tail;

    LRUCache(int cap) {
        this.capacity = cap;
        this.cache = new HashMap<>();
        this.head = new Node(-1, -1);
        this.tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
    }
    
    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    private void add(Node node) {
        node.next = this.head.next;
        this.head.next.prev = node;
        this.head.next = node;
        node.prev = this.head;
    }

    // Function to return value corresponding to the key.
    public int get(int key) {
        if(!cache.containsKey(key))
            return -1;
        
        Node getNode = cache.get(key);

        remove(getNode);
        add(getNode);
        
        return getNode.value;
    }

    // Function for storing key-value pair.
    public void put(int key, int value) {
        if(cache.containsKey(key)) {
            Node getNode = cache.get(key);
            remove(getNode);
        } else if(cache.size() == this.capacity) {
            cache.remove(tail.prev.key);
            remove(tail.prev);
        }
        
        Node newNode = new Node(key, value);
        add(newNode);
        cache.put(key, newNode);
    }
}
