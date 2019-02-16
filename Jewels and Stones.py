class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        
        J = list(J)
        jewels = {}
        
        for char in J:
            if char not in jewels:
                jewels[char] = 1
                
        S = list(S)
        
        output = 0
        
        for stone in S:
            if stone in jewels.keys():
                output += 1
                
                
        return output
        
            
        
