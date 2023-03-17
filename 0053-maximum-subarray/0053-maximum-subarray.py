class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum: int = 0
        best_sum: int = -sys.maxsize
        for n in nums:
            curr_sum = max(n, curr_sum + n)
            best_sum = max(curr_sum, best_sum)
        return best_sum