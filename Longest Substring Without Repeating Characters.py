class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        charList = list(s)
        count = 0
        maxCount = 0
        d = dict()

        for c in charList:
            if c not in d:
                count += 1
            else:
                d = dict()
                
                maxCount = count if count > maxCount else maxCount
                count = 0
            d[c] = True
        return maxCount


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
