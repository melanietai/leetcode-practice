"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # two strings are anagrams if any only if their sorted strings are equal
        strs_map = {} # store key as tuple and compared with each sorted str after converting to tuple
        for s in strs:
            if tuple(sorted(s)) in strs_map.keys():
                strs_map[tuple(sorted(s))].append(s)
            else:
                strs_map[tuple(sorted(s))] = [s]
        return strs_map.values()