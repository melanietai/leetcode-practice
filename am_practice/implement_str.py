class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:(i+len(needle))] == needle:
                    return i