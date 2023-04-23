class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest: int = (1 << 31)
        len_nums: int = len(nums)

        nums.sort()

        for i in range(len_nums):
            left, right = i + 1, len_nums - 1

            while left < right:
                curr_sum: int = nums[left] + nums[right] + nums[i]
                if abs(target - closest) >= abs(target - curr_sum):
                    closest = curr_sum
                    
                if curr_sum > target:
                    right -= 1
                else:
                    left += 1
            
        return closest