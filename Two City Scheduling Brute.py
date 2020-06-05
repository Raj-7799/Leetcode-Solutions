class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        return self.findMinCost(0, costs, n, n, 0)
    
    def findMinCost(self, idx, costs, cityALeft, cityBLeft, currentCost):
        minCost = currentCost
        if cityALeft > 0 and cityBLeft > 0:
            cityACost = self.findMinCost(idx + 1, costs, cityALeft - 1, cityBLeft, currentCost + costs[idx][0])
            cityBCost = self.findMinCost(idx + 1, costs, cityALeft, cityBLeft - 1, currentCost + costs[idx][1])
            return min(cityACost, cityBCost)
        elif cityALeft > 0:
            return self.findMinCost(idx + 1, costs, cityALeft - 1, cityBLeft, currentCost + costs[idx][0])
        elif cityBLeft > 0:
            return self.findMinCost(idx + 1, costs, cityALeft, cityBLeft - 1, currentCost + costs[idx][1])            
        else:
            return minCost
