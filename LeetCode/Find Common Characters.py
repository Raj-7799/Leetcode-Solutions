class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        
        ans = []
        solution = []
        
        x = list(A[0])
        lookup = {}
        for y in x:
            if y in lookup:
                lookup[y] += 1
            else:
                lookup[y] = 1
                
        for i in range(1, len(A)):
            z = list(A[i])
            commonDict = {}
            for j in z:
                if j in lookup:
                    if j in commonDict:
                        commonDict[j] += 1
                    else:
                        commonDict[j] = 1
            ans.append(commonDict)
        
        for key in lookup.keys():
            breakFlag = False
            repeat = lookup[key]
            for commonDict in ans:
                if key in commonDict:
                    repeat = min(repeat, commonDict[key])
                else:
                    breakFlag = True
                    break
            if breakFlag:
                continue
            else:
                for i in range(repeat):
                    solution.append(key)
        
        return solution
