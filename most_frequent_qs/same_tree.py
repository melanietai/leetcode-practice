# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         que = deque([(p, q)])
        
#         while que:
#             p, q = que.popleft()
#             if p and q:
#                 if p.val == q.val:
#                     que.append((p.left, q.left))
#                     que.append((p.right, q.right))
#                 else:
#                     return False
#             elif p or q:
#                 return False
            
#         return True

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)