# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            nonlocal preorder_ind
            
            if left > right:
                return None
            
            root_val = preorder[preorder_ind]
            root = TreeNode(root_val)
            
            preorder_ind += 1
            
            root.left = helper(left, inorder_map[root_val] - 1)
            root.right = helper(inorder_map[root_val] + 1, right)
            
            return root
        
        preorder_ind = 0
                               
        inorder_map = {}
        for i, v in enumerate(inorder):
            inorder_map[v] = i
        
        return helper(0, len(inorder)-1)