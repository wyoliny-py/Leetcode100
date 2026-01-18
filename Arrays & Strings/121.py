# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
    
        return max_profit

        # Time: O(n)
        # Space: O(1)
