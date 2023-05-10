from functools import reduce


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        accumulator = lambda xs, c: xs[:-1] if c == "#" else xs + c
        return reduce(accumulator, s, "") == reduce(accumulator, t, "")