class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        li = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[li] = nums[i]
                li+=1
        return li