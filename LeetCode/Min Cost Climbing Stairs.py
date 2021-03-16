class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        
        expense = [0 for i in range(len(cost))]
        
        expense[-1] = cost[-1]
        expense[-2] = cost[-2]
        
        for i in range(len(cost) -3, -1, -1):
            expense[i] = cost[i] + min(expense[i + 1], expense[i + 2])
            
        return min(expense[0], expense[1])
