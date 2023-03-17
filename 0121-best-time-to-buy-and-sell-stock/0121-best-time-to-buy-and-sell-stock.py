class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left: int = 0
        right: int = 1
        max_profit: int = 0
        days: int = len(prices)

        while right < days:
            if prices[right] < prices[left]:
                left = right
            else:
                max_profit = max(prices[right] - prices[left], max_profit)
            right += 1

        return max_profit
