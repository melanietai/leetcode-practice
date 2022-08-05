"""
12. Integer to Roman
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        v_to_s = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        
        res = ""
        
        for k in v_to_s.keys():
            if num >= k:
                res += (num // k) * v_to_s[k]
                remainder = num - (num // k) * k
                num = remainder
        
        return res