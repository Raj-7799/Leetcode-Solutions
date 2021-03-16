# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sum = 0
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumRootLeaft(root, '')
        return self.sum
    
    def sumRootLeaft(self, root, num):
        if root.left is None and root.right is None:
            self.sum += int(num + str(root.val), 2)
        if root.left:
            self.sumRootLeaft(root.left, num + str(root.val))
        if root.right:
            self.sumRootLeaft(root.right, num + str(root.val))
        
