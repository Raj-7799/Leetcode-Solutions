# Although there is a solution with binary search that solution doesn't work for inputs such as this [1,9,1,3,5,6,4]
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = 0
        
        for i in range(1, len(nums)):
            if nums[i] > nums[peak]:
                peak = i
        
        return peak
