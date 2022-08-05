class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}
        
        for i, n in enumerate(nums):
            m = target - n
            if m in num_map and i != num_map[m]:
                return [i, num_map[m]]
            num_map[n] = i