class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = prev2 = 0
        
        for i in range(2, len(cost) + 1):
            curr = min(prev + cost[i - 1], prev2 + cost[i - 2])
            prev, prev2 = curr, prev

        return curr