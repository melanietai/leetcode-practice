# Queue
# implement as linked list and circular array
# can use collections.deque object - doubly linked lists

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self, inlist):
        self._tail = None
        self._length = len(inlist)
    
        prev = None
        for item in inlist[::-1]:
            node = Node(item, next = prev)
            if self._tail is None:
                self._tail = node
            prev = node
        self._head = prev
    
    def enqueue(self, item):
        """Add item to end of queue."""
        self._length += 1
        node = Node(item)
        if self._tail:
            self._tail.next = node
            self._tail = node
        else:
            self._head = self._tail = node 
    
    def dequeue(self):
        """Remove item from front of queue and reutrn it."""
        self._length -= 1
        node = self._head
        self._head = self._head.next
        if not self._head:
            self._tail = None
        return node.data
    
    def length(self):
        return self._length
    
    def peek(self):
        """Return but don't remove item at front of queue."""
        if self.is_empty():
            return None
        return self._head.data
    
    def empty(self):
        """Empty queue."""
        self._head = self._tail = None
        self._length = 0
    
    def is_empty(self):
        """Is queue empty?"""
        return not bool(self._length)

# Algorithm
# Write a task manager with a Queue

task_queue = Queue()

while True:
    if task_queue.is_empty():
        next_task = None
    else:
        next_task = task_queue.peek()
    print("Next task:", next_task)

    command = input("A)dd task, D)o first task, or Q)uit? ")

    if command == "A":
        task = input("Task: ")
        task_queue.enqueue(task)
    
    elif command == "D":
        print("Completed:", task_queue.dequeue)
    
    elif command == "Q":
        break
    
    else:
        print("*** Invalid command; try again ***")
