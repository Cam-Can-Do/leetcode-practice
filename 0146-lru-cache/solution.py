class Node(object):
    def __init__(self, key = None, val = None, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev 
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.store = {}
        self.cap = capacity
        self.lru_ptr = Node()
        self.mru_ptr = Node()

        self.lru_ptr.next = self.mru_ptr
        self.mru_ptr.prev = self.lru_ptr

    def insert(self, node):
        node.prev = self.mru_ptr.prev
        node.next = self.mru_ptr
        self.mru_ptr.prev.next = node
        self.mru_ptr.prev = node

    def remove(self, node):
        temp = node.next
        node.next.prev = node.prev
        node.prev.next = temp

    def get(self, key: int) -> int:
        if key in self.store:
            self.remove(self.store[key])
            self.insert(self.store[key])
            return self.store[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key isn't stored, we need to store and insert it 
        if key in self.store:
            self.remove(self.store[key])
        elif self.cap == len(self.store):
            del self.store[self.lru_ptr.next.key]
            self.remove(self.lru_ptr.next)
        self.store[key] = Node(key, value)
        self.insert(self.store[key])

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
