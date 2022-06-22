"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
"""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1_ind = None
        w2_ind = None
        
        shortest_dis = len(wordsDict)
        
        for i, w in enumerate(wordsDict):
            if w == word1:
                w1_ind = i
            if w == word2:
                w2_ind = i
            if w1_ind != None and w2_ind != None:
                shortest_dis = min(abs(w1_ind-w2_ind), shortest_dis)
                
        return shortest_dis