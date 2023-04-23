class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count: int = 0
        prod: int = 1
        left: int = 0

        for right in range(len(nums)):
            prod *= nums[right]
            
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            
            count += right - left + 1

        return count