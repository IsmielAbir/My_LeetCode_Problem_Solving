class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li = []
        f = False
        for i in range(len(nums)):
            if nums[i]==target:
                li.append(i)
                f = True
        if f == True:
            return [li[0], li[-1]]
        else:
            return [-1,-1]
        