from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        
        solution = []
        
        for key in n1:
            if key in n2.keys():
                for i in range(min(n1[key], n2[key])):
                    solution.append(key)
                    
        return solution
