from collections import deque
from typing import Deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def actual_string(s: str) -> Deque[str]:
            stack = deque()
            for c in s:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack

        return actual_string(s) == actual_string(t)