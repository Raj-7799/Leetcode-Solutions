class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last, res, st = {}, 0, 0
        for i, v in enumerate(string):
            if v not in last or last[v] < st:
                res = max(res, i - st + 1)
            else:
                st = last[v] + 1
            last[v] = i
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("dvdf"))
