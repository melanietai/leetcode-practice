class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def rotation_ind(left, right):    
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = left + (right-left) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
                    
        def search(left, right):
            while left <= right:
                pivot = left + (right-left) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if nums[pivot] > target:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1
        
        n = len(nums)
            
        if n == 1:
            return 0 if nums[0] == target else -1
        
        rotate_ind = rotation_ind(0, n-1)
        
        if nums[rotate_ind] == target:
            return rotate_ind
        
        if rotate_ind == 0:
            return search(0, n-1)
        if target < nums[0]:
            return search(rotate_ind, n-1)
        
        return search(0, rotate_ind)
            