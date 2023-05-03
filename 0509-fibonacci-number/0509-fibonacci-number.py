from typing import List


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        memo: List[int] = [None] * n
        memo[0] = 0
        memo[1] = 1

        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n - 1] + memo[n - 2]