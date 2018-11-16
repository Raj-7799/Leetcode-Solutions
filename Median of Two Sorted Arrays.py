class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p1 = 0
        p2 = 0
        finalArr = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                finalArr.append(nums1[p1])
                p1 += 1
            else:
                finalArr.append(nums2[p2])
                p2 += 1

        while p1 < len(nums1):
            finalArr.append(nums1[p1])
            p1 += 1
        
        while p2 < len(nums2):
            finalArr.append(nums2[p2])
            p2 += 1

        if len(finalArr) % 2 == 0:
            return (finalArr[len(finalArr) // 2 -1] + finalArr[len(finalArr) // 2]) / 2
        
        else:
            return finalArr[len(finalArr) // 2 + 1]


