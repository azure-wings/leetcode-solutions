class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])

        return max_profit
