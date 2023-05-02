# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recValidBST(node: Optional[TreeNode], lo: int, hi: int) -> bool:
            if node is None:
                return True
            else:
                if lo < node.val < hi:
                    return recValidBST(node.left, lo, node.val) and recValidBST(node.right, node.val, hi)
                else:
                    return False

        return recValidBST(root, -1*(1 << 31) - 1, (1 << 31))