# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def search(self, root, val):
        if root is None:
            return 0
        else:
            if root.val < val:
                return self.search(root.right, val)
            elif root.val > val:
                return self.search(root.left, val)
            elif root.val == val:
                return 1 + self.search(root.left, val) + self.search(root.right, val)
    
    
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        queue = []
        
        if root is None:
            return False
        
        else:
            queue.append(root)
            
            while queue:
                curr = queue.pop()
                
                count = self.search(root, k - curr.val)
                
                if count > 0:
                    if curr.val == k - curr.val:
                        if count > 1:
                            return True
                    else:
                        return True
                
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                        
            return False
