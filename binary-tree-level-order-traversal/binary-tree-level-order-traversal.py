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
        if not root:
            return result

        visiting: Deque[TreeNode] = deque()
        visiting.append(root)

        while visiting:
            curr_level: List[TreeNode] = []
            while visiting:
                curr_level.append(visiting.popleft())
            
            result.append([node.val for node in curr_level])
            for node in curr_level:
                if node.left:
                    visiting.append(node.left)
                if node.right:
                    visiting.append(node.right)

        return result
            