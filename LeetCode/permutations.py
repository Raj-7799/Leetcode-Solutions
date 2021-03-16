class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []
        
        if len(nums) <= 1:
            solution.append(nums)
            return solution
        
        for i in range(len(nums)):
            
            ans = []
            temp = nums[0]
            nums[0] = nums[i]
            nums[i] = temp
            
            ans.append(nums[0])

            sub_solution = self.permute(nums[1:])
            for sub in sub_solution:
                solution.append(ans + sub)
                
        return solution
