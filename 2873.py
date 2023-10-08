class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    c = max(c, (nums[i]-nums[j])*nums[k])
        return c
        