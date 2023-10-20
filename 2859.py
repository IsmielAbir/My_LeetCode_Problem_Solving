class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0
        for i in range(len(nums)):
            if str(bin(i)[2:]).count('1')==k:
                s+=nums[i]
        return s
