class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums.sort()
        a = 1
        for i in nums:
            if a==i:
                a*=2
        return a
        