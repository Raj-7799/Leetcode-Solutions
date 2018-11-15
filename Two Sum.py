class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted(nums)
        
        for i in range(len(nums) - 1):
            found = self.search(nums, target - nums[i], i + 1, len(nums))
            if found > -1:
                return [i, found]

    

    def search(self, num, find, start, end):
        if start <= end:
            mid = (start + end - 1) // 2
            if num[mid] == find:
                return mid
            else:
                if num[mid] > find:
                    return self.search(num, find, start, mid)
                
                else:
                    return self.search(num, find, mid, end)
            
        else:
            return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3,2,3], 6))

