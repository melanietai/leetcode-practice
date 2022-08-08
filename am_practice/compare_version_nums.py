"""
165. Compare Version Numbers
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        
        while p1 < n1 or p2 < n2:
            chunk1, p1 = self.get_next_chunk(version1, n1, p1)
            chunk2, p2 = self.get_next_chunk(version2, n2, p2)
            if chunk1 != chunk2:
                return 1 if chunk1>chunk2 else -1
        return 0

        
    def get_next_chunk(self, version, n, p):
        if p > n-1:
            return 0, p
        
        p_end = p
        while p_end < n and version[p_end] != ".":
            p_end += 1
        chunk = int(version[p:p_end])
        p = p_end + 1
        return chunk, p
    