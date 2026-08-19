# 146. LRU Cache
# 已解答
# 中等
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise,
#  add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
# evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.





# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dic = {}
        
#         #creat dummy node.creating a double link list to 
#         #represent LRU
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
        
#         self.head.prev = self.tail
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.tail.next = self.head
    
#     #helper function
#     #remove specific node from the DLList
#     def remove(self, node):
#         cur = self.head.next
#         while cur.next != tail:
#             if cur.key == node.key:

#         cur.prev.next = cur.next
#         cur.next.prev = cur.prev
#         cur = 
#         cur.prev = None
#         cur.next = None
    
#     #add the node right after head in DLList
#     def add(self, node):
#         node.prev = head
#         node.next = head.next
#         head.next.prev = node
#         head.next = node

#     def get(self, key: int) -> int:
#         node = Node(key, 0)
#         if key in self.dic:
#             remove(node)
#             add(node)
#             return dic[key]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         node = Node(key, value)

#         if len(key) >= self.capacity:
#             remove(self.head.prev)
#             self.dic.remove(self.head.prev.key)
#         if key in self.dic:
#             cur = self.head.next
#             while cur != tail:
#                 if(cur.key == key):
#                     cur = cur.next
#                     remove(cur.prev)
#                 else:
#                     cur = cur.next
#             add(node)
#             dic[key] = value
#         else:
#             add(node)
#             dic[key] = value
        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        assert capacity > 0, "capacity must be > 0"
        self.capacity = capacity
        self.dic = {}  # key -> Node

        # dummy head and tail for easy inserts/removals
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # remove node from doubly-linked list
    def _remove(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        node.prev = None
        node.next = None

    # add node right after head (most-recently used position)
    def _add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        # move to head (mark most-recently used)
        self._remove(node)
        self._add_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            # move to head
            self._remove(node)
            self._add_to_head(node)
        else:
            # evict if at capacity
            if len(self.dic) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.dic[lru.key]
            # insert new node
            new_node = Node(key, value)
            self._add_to_head(new_node)
            self.dic[key] = new_node


# def main():
#     lines = sys.stdin.read().strip().split("\n")
    
#     # first line: LRUCache N
#     first = lines[0].split()
#     cap = int(first[1])
#     cache = LRUCache(cap)

#     # process the rest commands
#     for line in lines[1:]:
#         parts = line.split()
#         cmd = parts[0]

#         if cmd == "put":
#             key = int(parts[1])
#             value = int(parts[2])
#             cache.put(key, value)

#         elif cmd == "get":
#             key = int(parts[1])
#             print(cache.get(key))

# if __name__ == "__main__":
#     main()