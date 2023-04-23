from collections import deque
from typing import Deque, List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result: Deque[int] = deque()
        left, right = 0, len(nums) - 1
        square: Callable[[int], int] = lambda x: x*x
        
        while left <= right:
            left_square, right_square = \
                square(nums[left]), square(nums[right])
            if left_square >= right_square:
                result.appendleft(left_square)
                left += 1
            else:
                result.appendleft(right_square)
                right -= 1

        return list(result)