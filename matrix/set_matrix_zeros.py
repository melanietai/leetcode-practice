"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_ind = []
        col_ind = []
        
        for i, lst in enumerate(matrix):
            for j, num in enumerate(lst):
                if num == 0:
                    row_ind.append(i)
                    col_ind.append(j)

        for col in col_ind:
            for lst in matrix:
                lst[col] = 0
        
        for row in row_ind:
            matrix[row] = [0] * len(matrix[row])
        
        return matrix