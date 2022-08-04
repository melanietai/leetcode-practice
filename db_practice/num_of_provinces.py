"""
547. Number of Provinces
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        rows = len(isConnected)
        count = 0
    
        def dfs(row):
            for c, v in enumerate(isConnected[row]):
                if v == 1 and c not in seen:
                    seen.add(c)
                    dfs(c)
        
        for row in range(rows):
            if row not in seen:
                seen.add(row)
                dfs(row)
                count += 1
                
        return count