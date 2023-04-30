class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo: int = 0

        for i in range(3):
            hi: int = len(nums) - 1

            while lo <= hi:
                if nums[lo] == i:
                    lo += 1
                elif nums[lo] != i and nums[hi] == i:
                    nums[lo], nums[hi] = nums[hi], nums[lo]
                    lo += 1
                    hi -= 1
                else:
                    hi -= 1