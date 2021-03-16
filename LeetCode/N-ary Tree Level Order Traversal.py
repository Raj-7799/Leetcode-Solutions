"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        queue = []
        sol = []
        
        if root is None:
            return sol
        
        queue.append(root)
        
        while queue:
            sol.append([curr.val for curr in queue])
            
            for i in range(len(queue)):
                curr = queue.pop(0)
                
                if curr.children:
                    queue += curr.children
                    
        return sol
