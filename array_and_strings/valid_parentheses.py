"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {")": "(", "}": "{", "]": "["}
        for p in s:
            if len(stack) == 0 and p in p_map.keys():
                return False
            elif p in p_map.values():
                stack.append(p)
            elif p in p_map.keys():
                if p_map[p] == stack[-1]:
                        stack.pop()
                else:
                    return False
        return len(stack) == 0
        
#         open_stack = []
#         paren_table = {')':'(', '}':'{', ']':'['}
        
        
#         for c in s:
#             if c in paren_table.values():
#                 open_stack.append(c)
#             elif len(open_stack) == 0:
#                 return False
#             elif c in paren_table.keys():
#                 if paren_table[c] == open_stack[-1]:
#                     open_stack.pop()
#                 else:
#                     return False
#         if len(open_stack) == 0:
#             return True
#         else:
#             return False