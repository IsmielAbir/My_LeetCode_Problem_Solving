class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1= len(nums1)
        n2 = len(nums2)
        res = 0
     
        for num in nums1:
            if n2 % 2:
                res ^= num
                
        for num in nums2:
            if n1 % 2:
                res ^= num
        
        return res