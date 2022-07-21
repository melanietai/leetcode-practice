# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         def helper(root, ans=[]):
#             if not root:
#                 return ans

#             ans.append(root.val)
#             if root.left:
#                 helper(root.left, ans)
#             if root.right:
#                 helper(root.right, ans)
#             return ans
        
#         return helper(root)

        # recursive
#         def helper(root, ans=[]):
#             if root:
#                 ans.append(root.val)
#                 helper(root.left, ans)
#                 helper(root.right, ans)
#             return ans
#         return helper(root)
    
        # iterative
        
        stack = [root]
        ans = []
        
        if not root:
            return ans
        
        while stack:
            node = stack.pop()

            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans