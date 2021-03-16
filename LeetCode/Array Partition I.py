class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        for i in range(len(nums) // 2):
            ans += nums[2 * i]
            
        return ans
