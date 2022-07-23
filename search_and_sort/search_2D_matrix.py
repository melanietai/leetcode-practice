class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         rows, cols = len(matrix), len(matrix[0])
        
#         if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
#             return False
        
#         def find_row(low, high, target, matrix):
#             while low <= high:
#                 mid = low + (high-low) // 2
#                 if matrix[mid][0] <= target <= matrix[mid][cols-1]:
#                     return mid
#                 elif target < matrix[mid][0]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#         row = find_row(0, rows-1, target, matrix)
#         print(row)
#         if row == None:
#             return False
        
#         def find_col(row, low, high, target, matrix):
#             while low <= high:
#                 mid = low + (high-low) // 2
#                 print(row, mid, target)
#                 if matrix[row][mid] == target:
#                     return True
#                 elif target < matrix[row][mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             return False
        
#         return find_col(row, 0, cols-1, target, matrix)
        
        m = len(matrix)
        
        if m == 0:
            return False
        
        n = len(matrix[0])
        
        
        left, right = 0, m * n - 1
        # row = idx // n and col = idx % n
        
        while left <= right:
            mid = left + (right-left) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            else:
                if target < matrix[mid // n][mid % n]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False