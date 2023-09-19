class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s = set(nums1)
        d = set(nums2)
        li = [[], []]
        for i in s:
            if i not in d:
                li[0].append(i)
        for i in d:
            if i not in s:
                li[1].append(i)
        return li
    

        