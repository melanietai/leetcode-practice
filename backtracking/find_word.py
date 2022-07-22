class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find_match(board, r, c, word):
            
            if len(word) == 0:
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[0]:
                return False
            
            res = False
            
            board[r][c] = "#"
            
            for roffset, coffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                res = find_match(board, r+roffset, c+coffset, word[1:])
                if res:
                    break
            
            board[r][c] = word[0]
            
            return res
        
        rows = len(board)
        cols = len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if find_match(board, r, c, word):
                    return True
        return False