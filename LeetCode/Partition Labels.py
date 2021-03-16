class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        segmentInfos = {}
        
        # forming segments from string
        for i, letter  in enumerate(S):
            if letter not in segmentInfos:
                segmentInfos[letter] = Segment(i, i)
            else:
                segmentInfos[letter].updateEnd(i)
        
        # forming partitions
        answer = []
        i = 0
        l = 0
        r = segmentInfos[S[l]].end
        
        while(i < len(S)):
            if i > r:
                l = i
                r = segmentInfos[S[l]].end
            
            if i == r:
                answer.append(r - l + 1)
            elif segmentInfos[S[i]].end > r:
                r = segmentInfos[S[i]].end
            
            i += 1

        return answer
        
class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def updateEnd(self, newEnd):
        self.end = newEnd
        
