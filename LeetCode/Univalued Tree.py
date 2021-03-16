# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: 'TreeNode') -> 'bool':
        queue = []
        queue.append(root)
        idx = None
        
        while len(queue) > 0:
            
            curr = queue.pop(-1)
            
            if idx is None:
                idx = curr.val
                
            else:
                if curr.val != idx:
                    return False
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return True