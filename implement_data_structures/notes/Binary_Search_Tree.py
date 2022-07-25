"""Binary Search Tree.
Very efficient search.
Each node has a left and right child.
Has a "rule" of arragenment that dictates ordering.
Often used for fast searching.
"""
class BinarySearchNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right 
    
    def find(self, data):
        """Return node with this data. Start here. Return None if not found.
        Each step getting rid of half a tree.
        For n nodes, we need to search at most, log2n so our runtime is O(log n).
        We can search > 1000 nodes in only 10 steps, > 1000000 nodes in only 20 steps.
        Tree needs to be balanced to achieve that runtime."""
        curr = self
        while curr:
            if curr.data == data:
                return curr
            elif data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            