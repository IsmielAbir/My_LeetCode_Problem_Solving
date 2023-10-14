class Solution:
    def countElements(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            mn = min(nums)
            mx = max(nums)
            if (mn<nums[i] and mx>nums[i]):
                c+=1
        return c

        