# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':
        queue = []
        sol = []
        
        if root is None:
            return sol
        
        queue.append(root)
        
        while queue:
            sol.append(sum([curr.val for curr in queue]) / len(queue))
            
            for i in range(len(queue)):
                curr = queue.pop(0)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
        return sol
