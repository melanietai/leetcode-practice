"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        buy = None
        sell = None
        max_profit = 0
        
        # always need to assign buy first before sell
        
        for p in prices:
            if buy == None or buy > p:
                buy = p
                # assign sell back to None because just updated buy
                sell = None
                continue
            elif sell == None or sell < p:
                sell = p
                max_profit = max((sell-buy), max_profit)
        
        return max_profit