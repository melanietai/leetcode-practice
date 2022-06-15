"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
# time complexity: O(n)
# space complexity: O(n) - additional space to store new str
class Solution:
    def isPalindrome1(self, s: str) -> bool:
        anstr = ""
        for ch in s:
            if ch.isalnum():
                anstr += ch.lower()
        mid = len(anstr) // 2
        for i in range(mid):
            if anstr[i] != anstr[len(anstr)-i-1]:
                return False
        return True

# better solution with space complexity O(1)
# two pointers

class Solution:
    def isPalindrome2(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True