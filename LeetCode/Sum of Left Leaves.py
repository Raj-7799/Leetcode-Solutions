# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    total = 0
    
    def sumOfLeftLeaves(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0
        else:
            if root.left:
                if root.left.left is None and root.left.right is None:
                    self.total += root.left.val
                else:
                    self.sumOfLeftLeaves(root.left)
            if root.right:   
                self.sumOfLeftLeaves(root.right)
            
            return self.total
