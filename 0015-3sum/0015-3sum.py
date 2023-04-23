class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: List[int] = []
        len_nums: int = len(nums)
        
        nums.sort()

        for i in range(len_nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len_nums - 1
            target: int = -1 * nums[i]
            
            while left < right:
                curr_sum: int = nums[left] + nums[right]
                if curr_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return result