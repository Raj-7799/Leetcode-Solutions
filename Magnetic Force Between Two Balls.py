class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        answer = -1
        low = 1
        high = position[-1]
        
        while (low <= high):
            mid = low + (high - low) // 2
            # print(low, high, mid)
            if self.is_ok(position, mid, m):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return answer
                
    def is_ok(self, position, mid, m):
        prev = position[0]
        m -= 1
        for i in range(1, len(position)):
            if position[i] - prev >= mid:
                m -= 1
                prev = position[i]
                # print("m is {}".format(m))

        return m <= 0
