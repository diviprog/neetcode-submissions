# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            L, balanced_L = dfs(root.left)
            R, balanced_R = dfs(root.right)
            balanced = balanced_L and balanced_R and abs(L-R)<=1
            height = 1 + max(L,R)
            return height, balanced
        _, balanced = dfs(root)
        return balanced