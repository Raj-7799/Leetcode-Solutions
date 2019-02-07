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
            if root.left:
                solution += self.inorder(root.left)
                
            solution.append(root.val)
                
            if root.right:
                solution += self.inorder(root.right)
            
            return solution
    
    def increasingBST(self, root: 'TreeNode') -> 'TreeNode':
        tree = self.inorder(root)
        curr = solution = TreeNode(tree[0])
        for i in range(1, len(tree)):
            temp = TreeNode(tree[i])
            curr.left = None
            curr.right = temp
            curr = temp
        return solution