class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # unique_nums = sorted(set(nums))
        # nums[:len(unique_nums)] = unique_nums
        # return len(unique_nums)
        
        if len(nums) < 2:
            return len(nums)
        
        slow = 0
        fast = 0
        
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1