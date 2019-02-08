# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def insert(self, root, val):
        if root is None:
            root = val
        else:
            if root.val < val.val:
                if root.right is None:
                    root.right = val
                else:
                    self.insert(root.right, val)
                    
            else:
                if root.left is None:
                    root.left = val
                else:
                    self.insert(root.left, val)
        
    
    def trimBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'TreeNode':
        
        stack = []
        
        if root is None:
            return None
        else:
            stack.append(root)
            
            op = None
            
            while stack:
                
                curr = stack.pop()
                if curr.val >= L and curr.val <= R:
                    if op:
                        self.insert(op, TreeNode(curr.val))
                    else:
                        op = TreeNode(curr.val)
                
                if curr.right:
                    stack.append(curr.right)
                
                if curr.left:
                    stack.append(curr.left)
                    
            return op
