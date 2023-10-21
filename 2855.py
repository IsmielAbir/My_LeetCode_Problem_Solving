class Solution(object):
    def minimumRightShifts(self, nums):
        nums_sorted = sorted(nums)
        n = len(nums)
        for i in range(len(nums)):
            if nums == nums_sorted:
                return i
            nums = [nums[n-1]]+nums[:n-1]    
        return -1    
                
        