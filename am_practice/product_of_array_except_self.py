class Solution:
     def productExceptSelf(self, nums: List[int]) -> List[int]:
# O(1) space solution
        ans = [0] * len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = nums[i-1] * ans[i-1]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * right
            right *= nums[i]
        return ans
            
# O(n) space solution
#         ans = [0] * len(nums)
#         left = [0] * len(nums)
#         right = [0] * len(nums)
        
#         left[0] = 1
#         for i in range(1, len(nums)):
#             left[i] = nums[i-1] * left[i-1]
        
#         right[len(nums)-1] = 1
#         for i in range(len(nums)-2, -1, -1):
#             right[i] = nums[i+1] * right[i+1]
        
#         for i in range(len(nums)):
#             ans[i] = right[i] * left[i]
#         return ans
    
# brute force solution
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             ans.append(self.product(nums[:i]+nums[i+1:]))
#         return ans
    
#     def product(self, nums):
#         p = 1
#         for n in nums:
#             p *= n
#         return p
    