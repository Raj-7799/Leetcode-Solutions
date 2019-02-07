"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> 'List[int]':
        solution = []
        
        if root is None:
            return solution
        else:
            solution.append(root.val)
            
            for child in root.children:
                solution += self.preorder(child)
                
            return solution
        