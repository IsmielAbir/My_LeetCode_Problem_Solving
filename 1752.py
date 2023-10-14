class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        for i in range(len(nums)):
            if nums[i]<nums[i-1]:
                c+=1
        return True if c<=1 else False