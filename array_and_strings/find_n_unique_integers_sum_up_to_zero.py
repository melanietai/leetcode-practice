"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        # return an array where values are symmetric
        # if n is odd, we append 0 to the answer lst
        # max value is equal to n // 2 and min is -n // 2
        # use for loop, and each time append -i and i to answer lst
        
        if n % 2 != 0:
            lst = [0]
        else:
            lst = []
        
        for i in range(1, n // 2 + 1):
            lst.append(i)
            lst.append(-i)
        
        return lst

# alternative solution: return range(-n+1, n, 2)