# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def inorder(self, root):
        solution = []
        
        if root is None:
            return solution
        
        else:
            
            if root.left is None and root.right is None:
                solution.append(root.val) 
            
            if root.left:
                solution += self.inorder(root.left)
                
            if root.right:
                solution += self.inorder(root.right)
            
            return solution
    
    
    
    
    
    def leafSimilar(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
        
        tree1 = self.inorder(root1)
        
        tree2 = self.inorder(root2)
        
        return tree1 == tree2