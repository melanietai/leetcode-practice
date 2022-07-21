from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        queue = deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            if len(levels) == level:
                levels.append(deque())
            if level % 2 == 0:
                levels[level].append(node.val)
            else:
                levels[level].appendleft(node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # for i, l in enumerate(levels):
        #     if i % 2 != 0:
        #         levels[i] = levels[i][::-1]
        
        return levels