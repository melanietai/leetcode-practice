"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product = product * num
        return self.signFunc(product)

    def signFunc(self, num):
        if num == 0:
            return 0
        elif num < 0:
            return -1
        elif num > 0:
            return 1

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for n in nums:
            if not n:
                return 0
            if n < 0:
                sign = -sign
        return sign