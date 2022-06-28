"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
"""

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
#         Method 1:
#         row, col = len(grid), len(grid[0])
        
#         for _ in range(k):
            
#             new_grid = [[0]*col for _ in range(row)]
            
#             for r in range(row):
#                 for c in range(col-1):
#                     new_grid[r][c+1] = grid[r][c]
            
#             for r in range(row-1):
#                 new_grid[r+1][0] = grid[r][col-1]
            
#             new_grid[0][0] = grid[row-1][col-1]
            
#             grid = new_grid
        
#         return grid
        
#         Method 2:
#         row, col = len(grid), len(grid[0])
        
#         for _ in range(k):
#             prev = grid[-1][-1]
#             for r in range(row):
#                 for c in range(col):
#                     grid[r][c], prev = prev, grid[r][c]
            
#         return grid

        row, col = len(grid), len(grid[0])
        new_grid = [[0]*col for _ in range(row)]
        
        for r in range(row):
            for c in range(col):
                new_c = (c + k) % col
                wrap_around_count = (c + k) // col
                new_r = (r + wrap_around_count) % row
                new_grid[new_r][new_c] = grid[r][c]
        
        return new_grid