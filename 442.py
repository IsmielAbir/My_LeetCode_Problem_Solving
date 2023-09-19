class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        li = []
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i]==nums[i+1]:
                li.append(nums[i])
        return li
        