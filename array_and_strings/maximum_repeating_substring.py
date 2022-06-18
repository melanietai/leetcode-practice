"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.
"""
class Solution:
    def maxRepeating1(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        count = 0
        for i in range(1, len(sequence) // len(word) + 1):
            if word * i in sequence:
                count += 1
        return count

class Solution:
    def maxRepeating2(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        count = 1
        while word * count in sequence:
            count += 1
            
        return count -1 # last increment that breaks the while loop does not count