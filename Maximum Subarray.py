import math

class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        maxSubArraySum = [-math.inf for i in range(len(nums))]
        
        maxSubArraySum[0] = nums[0]
        
        for i in range(1, len(nums)):
            maxSubArraySum[i] = max(nums[i], maxSubArraySum[i - 1] + nums[i])
        
        return max(maxSubArraySum)
        
