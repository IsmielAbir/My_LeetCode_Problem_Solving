class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s^=i
        return s