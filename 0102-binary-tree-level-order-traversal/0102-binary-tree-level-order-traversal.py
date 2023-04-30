# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []
        if root is None:
            return result

        visiting: Deque[TreeNode] = deque()
        visiting.append(root)

        while visiting:
            curr_level: List[int] = []
            curr_size: int = len(visiting)
            for i in range(curr_size):
                curr_node: TreeNode = visiting.popleft()
                if curr_node.left is not None:
                    visiting.append(curr_node.left)
                if curr_node.right is not None:
                    visiting.append(curr_node.right)
                curr_level.append(curr_node.val)

            result.append(curr_level)

        return result
            