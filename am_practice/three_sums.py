"""
15. 3Sum
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.two_sums(nums, i, res)
        return res
    
    def two_sums(self, nums, i, res):
        s, e = i+1, len(nums)-1
        while s < e:
            addition = nums[i] + nums[s] + nums[e]
            if addition > 0:
                e -= 1
            elif addition < 0:
                s += 1
            else:
                res.append([nums[i], nums[s], nums[e]])
                e -= 1
                s += 1
                while s < e and nums[s] == nums[s-1]:
                    s += 1

# brute force: time exceeded limit
# from copy import deepcopy

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         def is_duplicate(t, triples):
#             a, b, c = t
#             for tri in triples:
#                 copy = deepcopy(tri)
#                 if a in copy:
#                     copy.remove(a)
#                     if b in copy:
#                         copy.remove(b)
#                         if c in copy:
#                             return True
#             return False
        
#         res = []
#         x = len(nums)
#         for i in range(x):
#             for j in range(i+1, x):
#                 for k in range(j+1, x):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         t = [nums[i], nums[j], nums[k]]
#                         if not is_duplicate(t, res):
#                             res.append(t) 
#         return res
        