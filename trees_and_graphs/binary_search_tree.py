class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def searchDFS(self, root, val):
        if not root or root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
    
    def searchBFS(self, root, val):
        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root
    
    def insert_recursion(self, root, val):
        if not root:
            return BinaryTreeNode(val)
        
        if val < root.val:
            root.left = self.insert_recursion(root.left, val)
        else:
            root.right = self.insert_recursion(root.right, val)
        
        return root
    
    def insert_iteration(self, root, val):
        node = root
        
        
        

