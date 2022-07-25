"""
Graph
- are like trees, except they can contain loops(cycles)
- relationships can be directed or undirected

- often use to model relationships between things 
- trees are acyclic graphs (types of trees that don't have cycles)
- all trees are graphs, but not all graphs are trees  
- trees have hierachy, graphs do not 

Basic Unit:
node (or vertex) - basic unit  
edge (or arc) - connects two nodes 
adjacent - two nodes are adjacent if they share an edge
adjacency list - for a given node, a list of every node it is directly connected to 
weight (optional) - each edge can have a weight (ex: price, or distance) * solves problems on efficiency *
"""
from collections import deque

class GraphNode:
    """Node in a graph."""
    def __init__(self, data, adjacent=None):
        if adjacent is None:
            adjacent = set()
        
        # don't want more than one connection between same nodes
        assert isinstance(adjacent, set) # adjacent must be a set!
        
        self.data = data
        self.adjacent = adjacent
    
class Graph:
    """Graph holding nodes."""
    def __init__(self):
        """Create an empty graph."""
        self.nodes = set()
    
    def add_node(self, node):
        """Add a node to our graph."""
        self.nodes.add(node)
    
    def connect_nodes(self, node1, node2):
        """Connect two nodes."""
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)
    
    def are_connected_BFS(self, node1, node2):
        """Would be DFS is used a stack."""
        possible_nodes = deque()
        seen = set()
        possible_nodes.append(node1)
        seen.add(node1)

        while possible_nodes:
            node = possible_nodes.popleft()
            if node is node2:
                return True  
            else:
                for n in node.adjacent - seen:
                    possible_nodes.append(n)
                    seen.add(n)
        return False 

    def are_connected_recursive_DFS(self, node1, node2, seen=None):
        if not seen:
            seen = set()
        
        if node1 is node2:
            return True 
        
        seen.add(node1)

        for n in node1.adjacent - seen:
            if self.are_connected_recursive_DFS(n, node2, seen):
                return True
        return False


if __name__=="__main__":
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)

    graph = Graph()
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)

    graph.connect_nodes(node1, node2)

    ans1 = graph.are_connected_BFS(node1, node2)
    ans2 = graph.are_connected_recursive_DFS(node1, node2)
    print(ans1)
    print(ans2)

    ans3 = graph.are_connected_BFS(node1, node4)
    ans4 = graph.are_connected_recursive_DFS(node1, node4)
    print(ans3)
    print(ans4)