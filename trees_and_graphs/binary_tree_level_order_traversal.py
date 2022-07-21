from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS trasversal, BFS write up
        # keep track of level
        # initiate levels -> the list that we return
        # if len(levels) == current level: add empty list
        # append node value based on level of each node
        
#         levels = []
        
#         if not root:
#             return levels
        
#         def helper(node, level):
            
#             if len(levels) == level:
#                 levels.append([])
#             levels[level].append(node.val)
            
#             if node.left:
#                 helper(node.left, level + 1)
#             if node.right:
#                 helper(node.right, level + 1)
            
#             return levels
        
#         return helper(root, 0)
        
        # BFS traversal
        # keep use a queue structure to add nodes - keep track of node
        # keep track of level
        levels = []
        
        if not root:
            return levels
        
        level = 0
        queue = deque([root])
        
        while queue:
            levels.append([])
            num_nodes_per_level = len(queue)
            
            for i in range(num_nodes_per_level):
                node = queue.popleft()
                levels[level].append(node.val)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return levels

        # BFS using queue that stores both node and level
            # levels = []
#         queue = deque([(root, 0)])
        
#         while queue:
#             node, level = queue.popleft()
#             if len(levels) == level:
#                 levels.append([])
#             levels[level].append(node.val)
#             print(levels)
            
#             if node.left:
#                 queue.append([node.left, level + 1])
#             if node.right:
#                 queue.append([node.right, level + 1])
            
#         return levels