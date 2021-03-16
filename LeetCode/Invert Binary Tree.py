# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        else:
            sol = TreeNode(root.val)
            sol.left = self.invertTree(root.right)
            sol.right = self.invertTree(root.left)
            
            return sol
                
