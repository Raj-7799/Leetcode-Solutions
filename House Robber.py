class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        if nums:
            if len(nums) == 1:
                return max(nums)
            else:

                maxValueArr = [0 for i in range(len(nums))]
                maxValueArr[-1] = nums[-1]
                maxValueArr[-2] = max(nums[-1], nums[-2])

                for i in range(len(nums) -3, -1, -1):
                    maxValueArr[i] = nums[i] + max(maxValueArr[i + 2:])

                return max(maxValueArr)
        else:
            return 0
