"""
Given a string s, return true if a permutation of the string could form a palindrome.
"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
        
        num_odd = 0
        for count in counter.values():
            if count % 2 != 0:
                num_odd += 1
        
        # do not need to check even or odd length because if even length, number of odd_nums will either be 0 or multiple of 2s
        # if len(s) % 2 == 0:
        #     return num_odd < 1
        # else:
        return num_odd < 2