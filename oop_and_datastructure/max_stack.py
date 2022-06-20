"""
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
"""

class MaxStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        return max(self.stack)
        

    def popMax(self) -> int:
        # if more than one max ele, only remove the top-most one (the last one added)
        # reverse the list and remove the first largest ele (pop)
        # reverse back the list
        # return the removed ele (from the pop)
        self.stack = self.stack[::-1]
        max_ele = self.stack.pop(self.stack.index(self.peekMax()))
        self.stack = self.stack[::-1]
        return max_ele