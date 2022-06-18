"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        w_to_p = {}
        
        if len(words) != len(pattern):
            return False
        if len(set(words)) != len(set(pattern)):
            return False
    
        for i in range(len(words)):
            if words[i] not in w_to_p:
                w_to_p[words[i]] = pattern[i]
            elif w_to_p[words[i]] != pattern[i]:
                return False
        return True