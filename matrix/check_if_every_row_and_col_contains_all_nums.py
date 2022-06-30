"""
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
"""

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        all_row = True
        all_col = True
        n = len(matrix)
        compare = set(range(1, n+1))
        
        for row in matrix:
            if compare != set(row):
                all_row = False
            
        for col in range(len(matrix[0])):
            col_content = set()
            for row_num, row in enumerate(matrix):
                col_content.add(matrix[row_num][col])
            if compare != col_content:
                all_col = False
        
        return all_row and all_col