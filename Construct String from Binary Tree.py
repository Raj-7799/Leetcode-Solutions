# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def tree2str(self, t: 'TreeNode') -> 'str':
        if t is None:
            return ""
        else:
            sol = str(t.val)
            if t.left:
                sol += '(' + self.tree2str(t.left)+ ')'
            else:
                if t.right:
                    sol += '()'
            if t.right:
                sol += '(' +self.tree2str(t.right)+ ')'
                
            return sol
