class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        letter_strs = []
        for d in digits:
            letter_strs.append(letters[d])
            
        while len(letter_strs) > 1:
            l1 = letter_strs.pop()
            l2 = letter_strs.pop()
            combos = []
            for i in l1:
                for j in l2:
                    combos.append(j+i)
            letter_strs.append(combos)
        
        return [] if not letter_strs else letter_strs[0]