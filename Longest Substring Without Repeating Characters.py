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
            if c not in dict:
                count += 1
                d[c] = True
            else:
                