# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        queue1 = []
        queue2 = []
        
        if p is None and q is None:
            return True
        else:
            if p and q:
                queue1.append(p)
                queue2.append(q)
                
                while queue1 and queue2:
                    curr1 = queue1.pop()
                    curr2 = queue2.pop()
                    
                    if curr1.val != curr2.val:
                        return False
                    else:
                        if curr1.left:
                            if curr2.left:
                                queue1.append(curr1.left)
                                queue2.append(curr2.left)
                            else:
                                return False
                            
                        if curr2.left:
                            if curr1.left:
                                queue1.append(curr1.left)
                                queue2.append(curr2.left)
                            else:
                                return False
                                
                        if curr1.right:
                            if curr2.right:
                                queue1.append(curr1.right)
                                queue2.append(curr2.right)
                            else:
                                return False
                        
                        if curr2.right:
                            if curr1.right:
                                queue1.append(curr1.right)
                                queue2.append(curr2.right)
                            else:
                                return False
                                      
                
                if queue1 or queue2:
                    return False
                else:
                    return True
                
            else:
                return False
