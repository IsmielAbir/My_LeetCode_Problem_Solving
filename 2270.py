class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        ls = 0
        c = 0
        for i in range(len(nums)-1):
            ls+=nums[i]
            s-=nums[i]
            if ls>=s:
                c+=1
        return c