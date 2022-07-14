class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_balanced_bu_helper(self, root):
        if not root:
            return True, -1 # is balanced, height -1
        # check subtree to see if they are balanced
        left_balanced, left_height = self.is_balanced_bu_helper(self, root.left)
        if not left_balanced:
            return False, 0
        right_balanced, right_height = self.is_balanced_bu_helper(self, root.right)
        if not right_balanced:
            return False, 0
        # check if the tree is balanced based on both subtrees
        return (abs(left_height - right_height) < 2), 1 + max(left_height, right_height)
    
    def is_balanced_bu(self, root):            
        return self.is_balanced_bu_helper(root)[0]
    
    def height(self, root):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def is_balanced_td(self, root):
        if not root:
            return True 
        # check if subtrees have height within 1. if true, check if subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 and \
            self.is_balanced_td(root.left) and \
            self.is_balanced_td(root.right)

        