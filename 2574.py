class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            li.append(abs(sum(nums[0:i])-sum(nums[i+1:])))
        return li

        