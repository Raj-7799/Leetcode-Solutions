class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return -1
        else:
            # FORWARD PASS
            forward_count = 0
            for i in range(len(rating)):
                for j in range(i + 1, len(rating)):
                    if rating[j] > rating[i]:
                        for k in range(j + 1, len(rating)):
                            if rating[k] > rating[j]:
                                forward_count += 1
            
            # BACKWARD PASS
            backward_rating = rating[::-1]
            backward_count = 0
            for i in range(len(backward_rating)):
                for j in range(i + 1, len(backward_rating)):
                    if backward_rating[j] > backward_rating[i]:
                        for k in range(j + 1, len(backward_rating)):
                            if backward_rating[k] > backward_rating[j]:
                                backward_count += 1
            return backward_count + forward_count
