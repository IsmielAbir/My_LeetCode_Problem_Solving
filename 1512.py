class Solution(object):
    def numIdenticalPairs(self, nums):
        a=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] == nums[j]):
                    a=a+1
        return a