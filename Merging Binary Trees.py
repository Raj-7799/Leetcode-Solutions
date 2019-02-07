# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        if t1 or t2:
            if t1 is None and t2:
                return t2
            elif t2 is None and t1:
                return t1
            else:
                new_root = TreeNode(t1.val + t2.val)
                new_root.left = self.mergeTrees(t1.left, t2.left)
                new_root.right = self.mergeTrees(t1.right, t2.right)
                return new_root
        else:
            return None