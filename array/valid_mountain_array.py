"""
941. Valid Mountain Array
Easy

2166

145

Add to List

Share
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        # index of left and right pointers
        left, right = 0, len(arr) - 1
        while left + 1 < len(arr) -1 and arr[left] < arr[left + 1]:
            left += 1
        while right - 1 > 0 and arr[right] < arr[right - 1]:
            right -= 1
        return left == right and left != 0 and right != len(arr) - 1