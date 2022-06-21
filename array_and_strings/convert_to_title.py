"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        capitals = string.ascii_uppercase
        result = []
        while n > 0:
            result.append(capitals[(n-1) % 26])
            n = (n-1) // 26
        
        return("".join(reversed(result)))