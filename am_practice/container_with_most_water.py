"""
11. Container With Most Water
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        marea = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            w = r - l
            h = min(height[r], height[l])
            marea = max(marea, h*w)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return marea
        
#brute force solution: time limit exceeded
#         area = 0
#         x = len(height)
#         for i in range(x):
#             for j in range(i+1, x):
#                 h = min(height[i], height[j])
#                 w = j - i
#                 a = h * w
#                 area = max(a, area)
        
#         return area