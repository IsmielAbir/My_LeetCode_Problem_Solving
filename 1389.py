class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            li.insert(index[i], nums[i])
        return li
            