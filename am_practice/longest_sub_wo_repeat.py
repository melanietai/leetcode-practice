"""
3. Longest Substring Without Repeating Characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        d = {}
        res = 0
        st = 0
        
        for i, c in enumerate(s):
            if c in d:
                res = max(res, i-st)
                st = max(st, d[c] + 1)
            d[c] = i
        return max(res, len(s)-st)