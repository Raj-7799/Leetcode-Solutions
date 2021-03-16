# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        stack = []
        inorder = []
        current = root
        
        while (current or stack):
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop(-1)
            inorder.append(current.val)
            current = current.right
        
        
        return inorder  