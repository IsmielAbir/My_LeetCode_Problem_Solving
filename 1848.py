class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        s = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                s = min(abs(i - start), s)
        return s
        