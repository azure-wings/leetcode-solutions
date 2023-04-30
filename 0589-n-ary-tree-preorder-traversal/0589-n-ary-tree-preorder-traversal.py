"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
from typing import Deque


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result: List[int] = []
        visiting: Deque[int] = deque()
        visiting.append(root)

        while visiting:
            curr: Node = visiting.pop()
            result.append(curr.val)
            visiting.extend(curr.children[::-1])

        return result