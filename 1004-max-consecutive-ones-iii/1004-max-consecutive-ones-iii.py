class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left: int = 0
        right: int = 0
        zeroes: int = 0
        max_ones: int = 0

        while right < len(nums):
            is_zero: int = 1 if nums[right] == 0 else 0
            if zeroes + is_zero <= k:
                zeroes += is_zero
                right += 1
                max_ones = (
                    right - left if right - left > max_ones
                    else max_ones
                )
            else:
                is_zero = 1 if nums[left] == 0 else 0
                zeroes -= is_zero
                left += 1

        return max_ones
