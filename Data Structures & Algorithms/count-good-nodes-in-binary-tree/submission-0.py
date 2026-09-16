# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodnode(root, maximum) -> int:
            if root is None:
                return 0
            good = 1 if root.val >= maximum else 0
            return good + goodnode(root.left, max(maximum, root.val)) + goodnode(root.right, max(maximum, root.val))
        
        return goodnode(root, root.val)
        
