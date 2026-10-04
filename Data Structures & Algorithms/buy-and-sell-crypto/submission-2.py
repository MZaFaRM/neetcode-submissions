class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        for sell in range(1, len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > max_profit:
                max_profit = profit

            if prices[sell] < prices[buy]:
                buy = sell
        return max_profit

        