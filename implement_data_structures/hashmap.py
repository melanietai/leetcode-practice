"""
Two main issues: 
1) hash function design 
- organize storage space as an array
- map a key value pair to an index in array 
- use modulo operataor as hash function since the key value is integer type 

2) collision handling 
- use prime number as base of modulo (eg.  2069 or 2081 - at most 2 common factors) to minimize potential collisions
- in case of collision, use a bucket to hold all values - use array to implement the bucket data structure

STEPS:  
For a given key, apply hash function to generate a hash that corresponds to the adddress in our main storage. With this hash key, find the bucket where the value should be stored. Iterate through bucket to check if desired <k, v> pair exist.

"""
class Bucket:
    """Use array as bucket data structure to hold all k-v pairs in case of collision."""
    def __init__(self):
        self.bucket = []

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i][1] = value
                found = True
                break
        if not found:
            self.bucket.append([key, value])

    def get(self, key):
        for [k, v] in self.bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]     

class HashMap:
    """Use array as data structure of storage spaces.
    Use % operator as hash function.
    Use prime number as base of modulo to mimize collision.

    """
    def __init__(self):
        self.key_space = 2081
        self.hash_table = [Bucket() for i in range(self.key_space)] # storage spaces

    def put(self, key, value):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)
    
    def get(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].get(key)

    def remove(self, key):
        hash_key = key % self.key_space 
        self.hash_table[hash_key].remove(key)


