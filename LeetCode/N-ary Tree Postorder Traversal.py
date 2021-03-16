"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> 'List[int]':
        solution = []
        
        if root is None:
            return solution
        else:
            
            for child in root.children:
                solution += self.postorder(child)
                
            solution.append(root.val)
                
            return solution
        