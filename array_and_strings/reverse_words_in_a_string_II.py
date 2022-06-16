"""
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.
"""

class Solution:
    def reverse(self, l, left, right):
        while left < right:
                l[left], l[right] = l[right], l[left]
                left, right = left + 1, right -1
            
    def reverse_words(self, l):
        left, right = 0, 0
        while right < len(l):
            if l[right] == " ":
                self.reverse(l, left, right -1)
                right += 1
                left = right
            else:
                right += 1
        self.reverse(l, left, len(l) -1)
    
    def reverseWords(self, l):
        self.reverse(l, 0, len(l) - 1)
        self.reverse_words(l)

    # def reverse_each_word(self, l):
    #     start = end = 0
        
    #     while start < len(l):
    #         # go to the end of the word
    #         while end < n and l[end] != ' ':
    #             end += 1
    #         # reverse the word
    #         self.reverse(l, start, end - 1)
    #         # move to the next word
    #         start = end + 1
    #         end += 1