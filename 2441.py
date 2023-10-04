class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums[::-1]:
            if -i in nums:
                return i
        return -1
        