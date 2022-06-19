"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        # check all possible diviser of length of s (< length of 1/2 of str)

        N = len(s)
        for i in range(1, N // 2 + 1):
            if (N % i == 0) and (s[:i] * (N // i) == s):
                return True
        return False

# replace our string, remove first and last ch and find if original string is inside
# alternative solution: return s in (s*2)[1: -1]
