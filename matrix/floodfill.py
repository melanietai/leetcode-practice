"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""

class Solution(object):
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r, c):
            if image[r][c] == prev_color:
                image[r][c] = color
                
                if r-1 >= 0:
                    dfs(r-1, c)
                if r+1 < row:
                    dfs(r+1, c)
                if c-1 >= 0:
                    dfs(r, c-1)
                if c+1 < col:
                    dfs(r, c+1)
        
        
        row, col = len(image), len(image[0])
        prev_color = image[sr][sc]
        if prev_color != color:
            dfs(sr, sc)
        return image

#         row, col = len(image), len(image[0])
#         prev_color = image[sr][sc]
        
#         if prev_color != color:
#             q = collections.deque([(sr, sc)])
#             while q:
#                 r, c = q.popleft()
#                 image[r][c] = color
#                 if r-1 >= 0:
#                     q.append((r-1, c))
#                 if r+1 < row:
#                     q.append((r+1, c))
#                 if c-1 >= 0:
#                     q.append((r, c-1))
#                 if c+1 < col:
#                     q.append((r, c+1))
        
#         return image