"""
Tree

Basic Unit:
node - basic unit 
children - nodes directly below a node  
descendants - nodes below a node 
parent - node directly above a node 
ancestor - nodes above a node 
root node - node at the top of tree 
leaf node - node without any children

Use Cases:
- Organizational Chart 
- A Filesystem 
- HTML DOM  
- Taxonomy 

Note: Every linked list is a tree. But not every tree is a linked list.
"""
class Node:
    """Node in a tree.""" 
    def __init__(self, data, children=None):
        self.data = data 
        self.children = children or []
    
    # Assume we have already built the tree
    def find_DFS_iterative(self, data):
        """DFS uses stack."""
        """Traverse an entire tree start at root node.
        Return node object with this data.
        Return none if not found"""
        to_visit = [self]
        while to_visit:
            curr = to_visit.pop()
            if curr.data == data:
                return curr
            to_visit.extend(curr.children)
    
    def find_BFS(self, data):
        """BFS uses queue."""
        """Use case: find the highest ranking "data" in the org chart."""
        """Changes the way we traverse the tree: use stack (DFS) vs queue (BFS)"""
        to_visit = [self]
        while to_visit:
            curr = to_visit.pop(0)
            if curr.data == data:
                return curr 
            to_visit.extend(curr.children)
    
    def find_DFS_recursive(self, data):
        pass

class Tree:
    def __init__(self, root):
        self.root = root
    
    def find_in_tree(self, data):
        """Return node object with this data. Start at root. Return None if not found."""
        return self.root.find_DFS_iterative(data)