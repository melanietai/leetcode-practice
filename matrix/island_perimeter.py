"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


"""

class Solution(object):
    def islandPerimeter(self, grid: List[List[int]]) -> int:
#         peri = 0
        
#         row_count, col_count = len(grid), len(grid[0])

#         def surround_check(r, c):
#             p = 0
#             if r-1 >= 0:
#                 if grid[r-1][c] != 1:
#                     p += 1
#             else:
#                 p += 1
#             if r+1 < row_count:
#                 if grid[r+1][c] != 1:
#                     p += 1
#             else:
#                 p += 1
#             if c-1 >= 0:
#                 if grid[r][c-1] != 1:
#                     p += 1
#             else:
#                 p += 1
#             if c+1 < col_count:
#                 if grid[r][c+1] != 1:
#                     p += 1
#             else:
#                 p += 1
#             return p
                
        
#         for row_num, row in enumerate(grid):
#             for col_num, val in enumerate(row):
#                 if val == 1:
#                     peri += surround_check(row_num, col_num)
        
#         return peri

        rows, cols = len(grid), len(grid[0])
        p = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    p += 4
                    if r > 0:
                        if grid[r-1][c] == 1:
                            p -= 2
                    if c > 0:
                        if grid[r][c-1] == 1:
                            p -= 2
        
        return p