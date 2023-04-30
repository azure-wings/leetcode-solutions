"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        if root is None:
            return result

        visiting = collections.deque()
        visiting.append(root)
        
        while visiting:
            curr = visiting.pop()
            if curr:
                result.append(curr.val)
                visiting.extend(reversed(curr.children))

        return result