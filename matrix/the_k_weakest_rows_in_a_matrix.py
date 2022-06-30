"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
"""

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # [[strength, index position]] sort by sum
        
        sol_ind = []
        
        for row_num, row in enumerate(mat):
            sol_ind.append([sum(row), row_num])
        
        sol_ind.sort()
        
        ans = []
        for i in range(k):
            ans.append(sol_ind[i][1])
            
        return ans
        
        
    """
    instead of sum function; can use binary search to find strength (index of first occuring 0)
    
    def binary_search(row):
        low = 0
        high = len(mat[0])
        while low < high:
            mid = low + (high-low) // 2
            if row[mid] == 1:
                low = mid + 1
            else:
                high = mid
        return low
    """