"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    result: List[int] = []

    def dfs(self, node: 'Node') -> None:
        if node is None:
            return
        else:
            self.result.append(node.val)
            for child in node.children:
                self.dfs(child)

    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        self.dfs(root)

        return self.result
        