class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        pointer_1 = pointer_2 = 0
        answer = []
        
        while pointer_1 < len(A) and pointer_2 < len(B):
            low = max(A[pointer_1][0], B[pointer_2][0])
            high = min(A[pointer_1][1], B[pointer_2][1])
            
            if low <= high:
                answer.append([low, high])
            
            if A[pointer_1][1] < B[pointer_2][1]:
                pointer_1 += 1
            else:
                pointer_2 += 1
                
        return answer
            
        
        
