# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        if root is None:
            return None
        else:
            if root.val == val:
                return root
            else:
                return self.searchBST(root.left, val) or self.searchBST(root.right, val)