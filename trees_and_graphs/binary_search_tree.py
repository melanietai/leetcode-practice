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

        while node:
            if val < node.val:
                if not node.left:
                    node.left = BinaryTreeNode(val)
                    return root
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = BinaryTreeNode(val)
                    return root
                else:
                    node = node.right

        return BinaryTreeNode(val)

    def delete_recursive(self, root, val):
        def successor(self, root):
            root = root.right
            while root.left:
                root = root.left
            return root 
        
        def predecessor(self, root):
            root = root.left 
            while root.right:
                root = root.right
            return root

        if not root:
            return root
        
        if val < root.left:
            root.left = self.delete_recursive(root.left, val)
        elif val > root.right:
            root.right = self.delete_recursive(root.right, val)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.delete_recursive(root.right, root.val)
            else:
                root.val = self.predessor(root)
                root.left = self.delete_recursive(root.left, root.val)
        return root
        
    def delete_iterative(self, root, val):
        pass
    
    def get_node(self, root, val):
        node = root

        while node:
            if node.val == val:
                return node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        raise Exception("No such value in the tree.")

class BinaryTree:
    