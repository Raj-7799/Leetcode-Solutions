class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNums = sorted(nums)

        for i in range(len(nums) - 1):
            found = self.search(sortedNums, target - nums[i], i + 1, len(nums))
            if found > -1:
                return [i, found]

    

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3, 2, 4], 6))
