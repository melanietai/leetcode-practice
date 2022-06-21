"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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
    def titleToNumber(self, n: str) -> int:
        
        alphabets = string.ascii_uppercase
        a_to_n = {}
        count = 0
        
        for i, alpha in enumerate(alphabets):
            a_to_n[alpha] = i + 1
        
        n = n[::-1]
        
        for i, ch in enumerate(n):
            count += a_to_n[ch] * 26 ** i
        
        return count