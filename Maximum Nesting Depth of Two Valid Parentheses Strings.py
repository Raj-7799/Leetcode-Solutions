class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        top_1 = -1
        top_2 = -1
        
        answer = []
        
        for bracket in list(seq):
            if bracket == "(":
                if top_1 < top_2:
                    top_1 += 1
                    answer.append(0)
                else:
                    top_2 += 1
                    answer.append(1)
            else:
                if top_1 > -1:
                    top_1 -= 1
                    answer.append(0)
                elif top_2 > -1:
                    top_2 -= 1
                    answer.append(1)
                    
        return answer
