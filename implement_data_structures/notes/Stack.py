"""Stack
Implemented using a Python list.
In cases where performance really matters, use a Python list directly to avoid the overhead of a custom class. For even better performance (smaller memory footprint, you can use collections.deque object)
"""

class Stack:
    def __init__(self, inlist = None):
        if inlist:
            self._list = inlist
        else:
            self._list = []
    
    def push(self, item):
        """Add item to end of stack."""
        self._list.append(item)
    
    def pop(self):
        """Remove item from end of stack and return it."""
        return self._list.pop()
    
    def length(self):
        """Return length of stack."""
        return len(self._list)
    
    def peek(self):
        """Return but don't remove top item."""
        if self.is_empty():
            return None
        else:
            return self._list[-1]
    
    def empty(self):
        """Empty stack."""
        self._list = []
    
    def is_empty(self):
        """Is stack empty?"""
        return not bool(self._list)

# Algorithm Example
# Balance Parens with a Stack

def are_parens_balanced(symbols):
    """Are parentheses balanced in expression?"""

    parens = Stack()

    for char in symbols:
        if char == "(":
            parens.push(char)
        elif char == ")":
            if parens.is_empty():
                return False
            else:
                parens.pop()
    return parens.is_empty()