# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def addnodes(node):
            arr.append(node)
            if node.left:
                addnodes(node.left)
            if node.right:
                addnodes(node.right)
        addnodes(root)
        return list(sorted(arr,key=lambda x:x.val))[k-1].val