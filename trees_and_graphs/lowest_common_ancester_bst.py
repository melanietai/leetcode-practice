# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root or not p or not q:
#             return None
        
#         v = root.val
#         if p.val < v and q.val < v:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif p.val > v and q.val > v:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root
        
        if not root or not p or not q:
            return None
        
        cur = root
        
        while cur:
            v = cur.val
            if p.val < v and q.val < v:
                cur = cur.left
            elif p.val > v and q.val > v:
                cur = cur.right
            else:
                return cur