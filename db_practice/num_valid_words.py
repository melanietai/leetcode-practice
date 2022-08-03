"""
1178. Number of Valid Words for Each Puzzle

"""
# Time limit exceeded

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        puzzle_map = {}
        for i, p in enumerate(puzzles):
            puzzle_map[(p, i)] = 0
            for w in words:
                if self.is_word_valid(p, w):
                    puzzle_map[(p, i)] += 1
        
        # return puzzle_map.values()
        ans = [v for k, v in sorted(puzzle_map.items(), key=lambda x:x[0][1])]

        return ans
    
    
    def is_word_valid(self, puzzle, word):
        if puzzle[0] in word:
            for ch in word:
                if ch not in set(puzzle):
                    return False
            return True
        return False
    