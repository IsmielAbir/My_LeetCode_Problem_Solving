class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = set(nums1)
        m = set(nums2)
        return n & m
        