class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        r = []

        while i < len(nums):
            if i == len(nums) - 1 or nums[i] != nums[i+1]:
                r.append(nums[i])
            else:
                i += 1
            i += 1

        return r
