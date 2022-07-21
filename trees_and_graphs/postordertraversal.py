# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, ans=[]):
            if root:
                helper(root.left, ans)
                helper(root.right, ans)
                ans.append(root.val)
            return ans
        return helper(root)
        
#         if not root:
#             return []
        
#         stack = []
#         ans = []
        
#         while True:
#             while root:
#                 if root.right:
#                     stack.append(root.right)
#                 stack.append(root)
                
#                 root = root.left
            
#             root = stack.pop()
            
#             if root.right and peek(stack) == root.right:
#                 stack.pop()
#                 stack.append(root)
#                 root = root.right
#             else:
#                 ans.append(root.val)
#                 root = None
             
#             if len(stack) <= 0:
#                 break
                
#         def peek(stack):
#             if len(stack) > 0:
#                 return stack[-1]
#             return None