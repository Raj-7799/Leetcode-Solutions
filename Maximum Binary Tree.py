import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMaxIndex(self, nums):
        idx = -1
        val =  -math.inf
        for i, value in enumerate(nums):
            if value > val:
                val = value
                idx = i
                
        return idx, val
    
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        idx, value = self.findMaxIndex(nums)
        if idx > -1:
            node = TreeNode(value)
            node.left = self.constructMaximumBinaryTree(nums[:idx])
            node.right = self.constructMaximumBinaryTree(nums[idx + 1 :])
            return node
        else:
            return None
