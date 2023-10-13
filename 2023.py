class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    c+=1
        return c
        