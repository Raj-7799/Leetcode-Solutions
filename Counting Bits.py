class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        lookup = []
        if num > -1:
            lookup.append(0)
        if num > 0:
            lookup.append(1)
        
        for i in range(2, num + 1):
            a = "{0:b}".format(i)
            lookup.append(int(a[0]) + lookup[int(a[1:], 2)])
        
        return lookup
        
        
