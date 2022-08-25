from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

#second solution
class DLinkedList:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev 
        self.next = next 
    
class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}

        self.head, self.tail = DLinkedList(), DLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node 
    
    def _remove_node(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_item(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            node.value = value
        else:
            new_node = DLinkedList()
            new_node.key = key
            new_node.value = value
            self.cache[key] = new_node
            self._add_node(new_node)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_item()
                del self.cache[tail.key]
                self.size -= 1

