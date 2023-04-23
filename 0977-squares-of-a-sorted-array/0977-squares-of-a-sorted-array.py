from collections import deque
from typing import Deque, List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums: Deque[int] = deque(nums)
        result: List[int] = []
        square: Callable[[int], int] = lambda x: x*x
        
        while nums:
            left_square, right_square = square(nums[0]), square(nums[-1])
            if left_square >= right_square:
                result.append(left_square)
                nums.popleft()
            else:
                result.append(right_square)
                nums.pop()

        return result[::-1]