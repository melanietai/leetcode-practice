"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_pos = len(nums)
        new_nums = [0] * num_pos
        
        for i, n in enumerate(nums):
            new_pos = (i + k) % num_pos
            new_nums[new_pos] = n
        
        nums[:] = new_nums

        return nums

#       brute force method: time limit exceeded
#         for _ in range(k):
#             prev = nums[-1]
#             for i in range(len(nums)):
#                 nums[i], prev = prev, nums[i]
            
#         return nums