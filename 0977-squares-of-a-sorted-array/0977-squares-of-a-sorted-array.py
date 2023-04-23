from collections import deque
from typing import Deque, List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums: Deque[int] = deque(nums)
        result: Deque[int] = deque()
        square: Callable[[int], int] = lambda x: x*x
        
        while nums:
            left_square, right_square = square(nums[0]), square(nums[-1])
            if left_square >= right_square:
                result.appendleft(left_square)
                nums.popleft()
            else:
                result.appendleft(right_square)
                nums.pop()

        return list(result)