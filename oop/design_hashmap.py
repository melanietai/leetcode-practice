"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""
class Bucket:
    def __init__(self):
        self.bucket = []

    def put(self, key: int, value: int) -> None:
        found = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i][1] = value
                found = True
                break
        if not found:
            self.bucket.append([key, value])

    def get(self, key: int) -> int:
        for [k, v] in self.bucket:
            if k == key:
                return v
        return -1
        
    def remove(self, key: int) -> None:
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]
        
class MyHashMap():
    
    def __init__(self):
        # use a large prime number as the base of modulo to minimize potential collisions
        self.key_space = 2081
        self.hash_table = [Bucket() for i in range(self.key_space)]
    
    def put(self, key, value):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].put(key, value)
    
    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)
    
    def remove(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].remove(key)

## by adding hash function - > reduce vast key space into a limited address space
## in case of collision (two keys mapped to same address), use a bucket to store all the values
## can use a LinkedList or Array to implement bucket data structure

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

