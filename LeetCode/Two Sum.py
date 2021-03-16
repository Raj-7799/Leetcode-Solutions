class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = dict()

        i = 0

        for num in nums:
            if (target - num) in numDict:
                if i != numDict[target - num]:
                    return sorted([i, numDict[target - num]])
            numDict[num] = i
            i += 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3, 3], 6))
