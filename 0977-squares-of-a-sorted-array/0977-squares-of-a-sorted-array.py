from collections import deque
from typing import Deque, List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result: List[int] = [0] * len(nums)
        left, right = 0, len(nums) - 1
        
        while left <= right:
            left_square, right_square = \
                nums[left]*nums[left], nums[right]*nums[right]
                
            if left_square >= right_square:
                result[right - left] = left_square
                left += 1
            else:
                result[right - left] = right_square
                right -= 1

        return result