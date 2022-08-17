# two pointers solution 1
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        for i in range(len(nums)-2):
            total += self.two_sum_smaller(nums, i+1, target-nums[i])
        return total
        
        
    def two_sum_smaller(self, nums, start_ind, target):
        s, e = start_ind, len(nums)-1
        total = 0
        while s < e:
            if nums[s] + nums[e] < target:
                total += e - s
                s += 1
            else:
                e -= 1
        return total

# two pointers solution 2
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        for i in range(len(nums)-2):
            s, e = i+1, len(nums)-1
            while s < e:
                addition = nums[i] + nums[s] + nums[e]
                if addition < target:
                    total += e-s
                    s += 1
                else:
                    e -= 1
        return total


