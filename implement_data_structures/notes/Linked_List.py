"""
Linked list

Things you might want to do:
- print each node 
- find a node by its data 
- append a node  
- remove a node 
- inserting a new node at a position other than the end

Runtime:
insert at beginning 
- O(1) - constant time 

append at end 
- O(1) - constant time 

delete from beginning 
- O(1) - constant time 

pop from end 
- O(n) - linear time
** we have to update the tail and we can't go backwards (for singly linked list; doubly linked list is constant time) **

get item by index 
- O(n) - linear time
"""
class Node:
    """Node in a linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    """Linked list."""

    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    def __init__(self, inlist):
        self.tail = None
        prev = None
        for item in inlist[::-1]:
            node = Node(item, next=prev)
            if not self.tail:
                self.tail = node
            prev = node 
        self.head = prev
            
    # Assume we have already built the list
    # We will now traverse the list and print it

    def print_list(self):
        """Traversing: Print all items in the list."""
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next
    
    def find(self, data):
        """Searching: Does this data exist in our list?"""
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    
    def append(self, data):
        node = Node(data)
        # if list starts as empty
        if not self.head:
            self.head = node
        # if list starts as non-empty
        if self.tail:
            self.tail.next = node 
        # update where tail points
        self.tail = node

    def remove(self, value):
        """Remove node with given value."""
        # remove first item or only item in linked list
        if self.head and self.head.data == value:
            self.head = self.head.next 
            if not self.head:
                self.tail = None 
            return 
        # remove an item in middle or the last item
        curr = self.head 
        while curr.next:
            if curr.next.data == value:
                curr.next = curr.next.next
                # if removing last item, update tail
                if not curr.next:
                    self.tail = curr
                    return
            else:
                # if haven't found yet, keep traversing
                curr = curr.next
    
    
