"""
167. Two Sum II - Input Array Is Sorted
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while l < r:
            s = numbers[l] + numbers[r]
            if numbers[l] + numbers[r] == target:
                return[l+1, r+1]
            elif s > target:
                r -= 1
            else:
                l += 1
        