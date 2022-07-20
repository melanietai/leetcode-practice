# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
# Recursive Traverssal / DFS
        def validate(root, lower=-math.inf, upper=math.inf):
            if not root:
                return True
            v = root.val
            if v <= lower or v >= upper:
                return False
            return validate(root.right, v, upper) and validate(root.left, lower, v)
        
        return validate(root)
            
        
# Iterative Traversal / BFS
#         if not root:
#             return True
        
#         stack = [(root, -math.inf, math.inf)]
        
#         while stack:
#             root, lower, upper = stack.pop()
            
#             if not root:
#                 continue
            
#             v = root.val
            
#             if v <= lower or v >= upper:
#                 return False
            
#             stack.append((root.right, v, upper))
#             stack.append((root.left, lower, v))
        
#         return True
        
        