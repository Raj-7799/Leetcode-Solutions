class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        finalArr = []
        oddArr = []
        
        for i in A:
            if i % 2 == 0:
                finalArr.append(i)
            else:
                oddArr.append(i)
                
        for i in oddArr:
            finalArr.append(i)
            
        return finalArr
