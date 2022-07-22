"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # recursive solution
#         def helper(head, visited={}):

#             if not head:
#                 return head

#             # if inside visited: return back node instead of creating a new one
#             if head in visited:
#                 return visited[head]

#             # create new node # add to visited
#             node = Node(head.val)

#             visited[head] = node
#             # recursive call node.next and node.random
#             node.next = helper(head.next, visited)
#             node.random = helper(head.random, visited)

#             return node
#         return helper(head)
    
        # iterative solution
        if not head:
            return head
        visited = {}
        old_node = head
        new_node = Node(head.val)
        ans = new_node
      
        visited[old_node] = new_node
        
        while old_node:
            
            if old_node.next:
                if old_node.next in visited:
                    new_node.next = visited[old_node.next]
                else:
                    new_node.next = Node(old_node.next.val)
                    visited[old_node.next] = new_node.next
            
            if old_node.random:
                if old_node.random in visited:
                    new_node.random = visited[old_node.random]
                else:
                    new_node.random = Node(old_node.random.val)
                    visited[old_node.random] = new_node.random
                
            new_node = new_node.next
            old_node = old_node.next
        
        return ans