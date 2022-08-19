class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        
        def find_area(x, y, area = 0):
            # if (x, y) in seen or grid[x][y] == 0:
            #     return area

            area += 1
            seen.add((x, y))
            
            offsets = (0, 1), (1, 0), (0, -1), (-1, 0)
            
            for xoff, yoff in offsets:
                new_x = x + xoff
                new_y = y + yoff
                if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in seen and grid[new_x][new_y]:
                # if 0 <= new_x < rows and 0 <= new_y < cols:
                    area = find_area(new_x, new_y, area)
            
            return area
        
        rows, cols = len(grid), len(grid[0])
        max_a = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and grid[r][c] not in seen:
                    a = find_area(r, c)
                    max_a = max(max_a, a)
                    
        return max_a


#         seen = set()
    
#         def area(r, c):
#             if not (0 <= r < rows and 0 <= c < cols and (r, c) not in seen and grid[r][c]):
#                 return 0
#             seen.add((r, c))
#             return (1 + area(r+1, c) + area(r-1, c) + area(r, c+1) + area(r, c-1))
    
#         rows, cols = len(grid), len(grid[0])
#         max_a = 0
#         for r in range(rows):
#             for c in range(cols):
#                 a = area(r, c)
#                 max_a = max(a, max_a)
#         return max_a