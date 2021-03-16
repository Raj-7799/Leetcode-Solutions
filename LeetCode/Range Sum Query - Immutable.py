class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = []
        if len(nums) > 0:
            self.nums.append(nums[0])

            for i in range(1, len(nums)):
                self.nums.append(self.nums[i - 1] + nums[i])
        
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if len(self.nums) == 0:
            return None
        
        if i == 0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
