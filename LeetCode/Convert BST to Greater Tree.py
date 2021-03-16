# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    total = 0
    
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        else:
            self.convertBST(root.right)
            val = root.val
            root.val += self.total
            self.total += val
            self.convertBST(root.left)
            
            return root
