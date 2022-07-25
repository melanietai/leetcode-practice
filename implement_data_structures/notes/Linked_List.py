"""
Linked list

"""
class Node:
    """Node in a linked list."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        