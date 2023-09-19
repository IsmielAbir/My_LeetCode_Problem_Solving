class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1+nums2
        n.sort()
        li = len(n)
        med = li//2
        if li%2==0:
            return (n[med]+n[med-1])/2
        else:
            return n[med]

        