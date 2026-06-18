from java.util import HashMap;
class LRUCache {
    
    //doubly-linked list
    private static class Node {
        Node prev, next;
        int key, value;
        private Node(int key, int value) {
            this.key = key;
            this.value = value;
            this.prev = null;
            this.next = null;
        }
    }

    Map<Integer, Node> dir = new HashMap<>();
    int capacity;
    Node head = new Node(5, 5);
    Node tail = new Node(5, 5);
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        Node node = dir.get(key);
        if(node == null) {
            return -1;
        } else {
            removeNode(node);
            moveToFront(node);
            return node.value;
        }
    }
    
    public void put(int key, int value) {
        Node node = dir.get(key);
        if(node != null) {
            node.value = value;
            removeNode(node);
            moveToFront(node);
        } else {
            Node newNode = new Node(key, value);
            dir.put(key, newNode);
            moveToFront(newNode);
            
            if(dir.size() > this.capacity) {
                Node lru = tail.prev;
                dir.remove(lru.key);
                removeNode(lru);
            }
        }
    }

    private void moveToFront(Node node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }

    private void removeNode(Node node) {
        // Node prev = node.prev;
        // Node next = node.next;
        // prev.next = next;
        // next.prev = prev;
        // node.prev = null;
        // node.next = null;

        //or this:
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.prev = null;
        node.next = null;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */