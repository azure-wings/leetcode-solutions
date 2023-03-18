class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left: int = 0
        currsum: int = 0
        minlen: int = sys.maxsize

        for right in range(len(nums)):
            currsum += nums[right]
            while currsum >= target:
                minlen = min(minlen, right-left+1)
                currsum -= nums[left]
                left += 1

        return minlen if minlen < sys.maxsize else 0