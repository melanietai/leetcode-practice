"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        new_r, new_c = col, row
        new_matrix = [[0] * new_c for _ in range(new_r)]
        
        for r in range(new_r):
            for c in range(new_c):
                new_matrix[r][c] = matrix[c][r]
                
        return new_matrix