class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                max_profit = max(prices[right] - prices[left], max_profit)

        return max_profit
