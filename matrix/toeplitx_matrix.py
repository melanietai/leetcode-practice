"""
766. Toeplitz Matrix
Easy

2002

120

Add to List

Share
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])
        for r in range(row - 1):
            for c in range(col - 1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
        return True