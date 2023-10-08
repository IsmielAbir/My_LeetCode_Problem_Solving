class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[-1]
        for i in range(len(nums)-1):
            n = min(n, abs(nums[i]-nums[i+1]))
        return n
        