class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        ls = 0
        for i in range(len(nums)):
            if ls==s-nums[i]:
                return i
            ls+=nums[i]
            s-=nums[i]
            
        return -1
        