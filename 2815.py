class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (max(str(nums[i]))==max(str(nums[j]))) and (nums[i]+nums[j])>mx:
                    mx = nums[i]+nums[j]
        return mx

