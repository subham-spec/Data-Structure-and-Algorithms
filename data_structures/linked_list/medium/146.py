# 146. LRU Cache

class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value 

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def remove(self, node):
        # if it's the only node
        if node.left == None and node.right == None:
            self.head = self.tail = None

        # if it's the head
        elif node.left == None:
            self.head = node.right
            self.head.left = None
            
        # if it's the tail
        elif node.right == None:
            self.tail = node.left
            self.tail.right = None

        # if it's in the middle
        else:
            node.left.right = node.right
            node.right.left = node.left

        self.length -= 1

    def insert(self, node):
        # if empty
        if self.head == None:
            self.head = self.tail = node
        else:
            node.left = None
            node.right = self.head
            self.head.left = node
            self.head = node
      
        self.length += 1

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = LinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # move node to be head
            self.list.remove(node)
            self.list.insert(node)

            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, remove prev node
        if key in self.cache:
            self.list.remove(self.cache[key])
        
        new_node = Node(key, value)
        self.list.insert(new_node)
        self.cache[key] = new_node

        if self.list.length > self.capacity:
            # remove last element
            key_to_remove = self.list.tail.key 
            node_to_remove = self.list.tail

            self.list.remove(node_to_remove)
            del self.cache[key_to_remove]

'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''